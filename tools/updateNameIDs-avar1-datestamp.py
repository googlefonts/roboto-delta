#!/usr/bin/env python
import argparse
from datetime import datetime
from fontTools.ttLib import TTFont

parser = argparse.ArgumentParser(description='A program to catch current location')
parser.add_argument("-f", "--family_name", help="Familyname to update", default="Familyname")
parser.add_argument("-s", "--style_name", help="Stylename to update", default="Stylename")
parser.add_argument("-i", "--input_font", help="location of the iutput font", default="Regular_input.ttf")
parser.add_argument("-o", "--output_font", help="location of the output font", default="Regular_output.ttf")
parser.add_argument("-d", "--datestamp", help="add datestamp?", default="True")
args = parser.parse_args()

def update_name_id(font_path, target_name_id, new_string, output_path):
    font = TTFont(font_path)
    name_table = font["name"]

    # Iterate through existing records and update the target nameID
    for record in name_table.names:
        if record.nameID == target_name_id:
            record.string = new_string

    font.save(output_path)
    print(f"Successfully updated nameID {target_name_id} in {output_path}")

def update_name_ids(name_id_1, name_id_2, name_id_4, name_id_6, name_id_16, name_id_17):
    
    update_name_id(args.input_font, target_name_id=1, new_string=name_id_1, output_path=args.output_font)
    update_name_id(args.input_font, target_name_id=2, new_string=name_id_2, output_path=args.output_font)
    update_name_id(args.input_font, target_name_id=4, new_string=name_id_4, output_path=args.output_font)
    update_name_id(args.input_font, target_name_id=6, new_string=name_id_6, output_path=args.output_font)
    update_name_id(args.input_font, target_name_id=16, new_string=name_id_16, output_path=args.output_font)
    update_name_id(args.input_font, target_name_id=17, new_string=name_id_17, output_path=args.output_font)
    

#print(args.datestamp)

if args.datestamp=="True":
    name_id_1 = args.family_name + " " + datetime.today().strftime('%Y-%m-%d')
    name_id_2 = args.style_name
    name_id_4 = args.family_name + " " + datetime.today().strftime('%Y-%m-%d')
    name_id_6 = args.family_name.replace(" ", "") + "-" + datetime.today().strftime('%Y-%m-%d') + args.style_name
    name_id_16 = args.family_name
    name_id_17 = args.style_name
    update_name_ids(name_id_1, name_id_2, name_id_4, name_id_6, name_id_16, name_id_17)
else:
    name_id_1 = args.family_name
    name_id_2 = args.style_name
    name_id_4 = args.family_name
    name_id_6 = args.family_name.replace(" ", "") + args.style_name
    name_id_16 = args.family_name
    name_id_17 = args.style_name
    update_name_ids(name_id_1, name_id_2, name_id_4, name_id_6, name_id_16, name_id_17)


