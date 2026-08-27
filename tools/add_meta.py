#!/usr/bin/env python3
"""Add a 'meta' table with design/supported language tags (dlng/slng).

Roboto Delta is a Latin-Greek-Cyrillic alpha currently covering Latin,
so both tags are 'Latn'. See
https://learn.microsoft.com/en-us/typography/opentype/spec/meta

Usage: python3 tools/add_meta.py font.ttf [font2.ttf ...]
"""

import sys

from fontTools.ttLib import TTFont, newTable

for path in sys.argv[1:]:
    font = TTFont(path)
    meta = font.get("meta") or newTable("meta")
    meta.data["dlng"] = "Latn"
    meta.data["slng"] = "Latn"
    font["meta"] = meta
    font.save(path)
    print(f"meta table set on {path}")
