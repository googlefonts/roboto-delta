#!/usr/bin/env python3
"""Rebuild the name tables of the generated static fonts so they conform to
the Google Fonts static-font spec:
https://googlefonts.github.io/gf-guide/statics.html#supported-styles

Axis values other than weight and italic (opsz, wdth, GRAD) become part of
the family name, per
https://googlefonts.github.io/gf-guide/statics.html#unsupported-styles

Style particle names come from the Google Fonts Axis Registry fallback
names. Two values in the Roboto Delta design space have no registered
fallback: wdth=151 uses "ExtraExpanded" (the Roboto Flex convention for its
identical 25-151 width space) and wght=1000 uses "ExtraBlack".

Usage:
    python tools/fix_static_names.py fonts/LGCAlpha/statics/*/*.ttf
"""

import argparse
import os
import re

from axisregistry import AxisRegistry, build_static_name_table
from fontTools.ttLib import TTFont

FAMILY_NAME = "Roboto Delta"
ITALIC_ANGLE = -12.0

# Values not in the axis registry fallbacks.
NAME_OVERRIDES = {
    "wdth": {151: "ExtraExpanded"},
    "wght": {1: "Hairline", 1000: "ExtraBlack"},
}

# Axes whose particles join the family name, in GF axis order.
FAMILY_AXES = ["GRAD", "opsz", "wdth"]

FS_SELECTION_ITALIC = 1 << 0
FS_SELECTION_BOLD = 1 << 5
FS_SELECTION_REGULAR = 1 << 6
MAC_STYLE_BOLD = 1 << 0
MAC_STYLE_ITALIC = 1 << 1

registry = AxisRegistry()


def particle_name(tag, value):
    axis = registry[tag]
    if value == axis.default_value:
        return None  # elided
    if value in NAME_OVERRIDES.get(tag, {}):
        return NAME_OVERRIDES[tag][value]
    for fallback in axis.fallback:
        if fallback.value == value:
            return fallback.name
    raise ValueError(f"No fallback name for {tag}={value}")


def parse_filename(path):
    stem = os.path.splitext(os.path.basename(path))[0]
    coords = {t: float(v) for t, v in re.findall(r"(GRAD|opsz|wdth|wght)(-?[\d.]+)", stem)}
    missing = {"GRAD", "opsz", "wdth", "wght"} - set(coords)
    if missing or not re.search(r"-(Roman|Italic)-", stem):
        raise ValueError(f"Cannot parse axis coordinates from {stem}")
    return coords, "-Italic-" in stem


def fix_font(path):
    coords, italic = parse_filename(path)
    font = TTFont(path)

    family_particles = [particle_name(tag, coords[tag]) for tag in FAMILY_AXES]
    family = " ".join([FAMILY_NAME] + [p for p in family_particles if p])

    weight_name = particle_name("wght", coords["wght"]) or "Regular"
    style = f"{weight_name} Italic" if italic else weight_name
    style = style.replace("Regular Italic", "Italic")

    build_static_name_table(font, family, style)

    subfamily = font["name"].getDebugName(2)
    os2, head, post = font["OS/2"], font["head"], font["post"]
    os2.fsSelection &= ~(FS_SELECTION_ITALIC | FS_SELECTION_BOLD | FS_SELECTION_REGULAR)
    head.macStyle &= ~(MAC_STYLE_BOLD | MAC_STYLE_ITALIC)
    if "Bold" in subfamily:
        os2.fsSelection |= FS_SELECTION_BOLD
        head.macStyle |= MAC_STYLE_BOLD
    if "Italic" in subfamily:
        os2.fsSelection |= FS_SELECTION_ITALIC
        head.macStyle |= MAC_STYLE_ITALIC
    if subfamily == "Regular":
        os2.fsSelection |= FS_SELECTION_REGULAR
    post.italicAngle = ITALIC_ANGLE if italic else 0.0

    font.save(path)
    name = font["name"]
    return [name.getDebugName(i) for i in (1, 2, 16, 17, 6)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fonts", nargs="+", help="static .ttf files to fix in place")
    args = parser.parse_args()
    failed = []
    for path in args.fonts:
        try:
            names = fix_font(path)
        except Exception as e:
            failed.append(path)
            print(f"{os.path.basename(path)}: FAILED: {e}")
            continue
        print(f"{os.path.basename(path)}")
        print(f"  1: {names[0]!r}  2: {names[1]!r}  16: {names[2]!r}  17: {names[3]!r}  6: {names[4]!r}")
    if failed:
        raise SystemExit(f"{len(failed)} of {len(args.fonts)} fonts failed")


if __name__ == "__main__":
    main()
