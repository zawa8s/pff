#!/usr/bin/python3
import fontforge
#from 115 import eng2hinsimblsdict
from ing2others_dict15 import ing2others_tpl15
print(ing2others_tpl15)
scripts = (
    # "ing",
    "hindi",
    "bangla","guzrati","gurmukhi","oriya",
    "korean",
    "telugu","tamil","kannada","malayalam","sinhala"
    # ,"eng","binaryv","binaryh","hex",
    # "notosans"
)
ing15 = fontforge.open(f"/home/viml/mg/zw8/pff/sfd/source15/ing15.sfd")
for x in scripts:
    x15 = fontforge.open(f"/home/viml/mg/zw8/pff/sfd/source15/{x}15.sfd")
    print(f"x is {x} and x15 family name is {x15.familyname}")
    ########
    ing15.selection.select(("ranges", None), " ", "@")
    ing15.copy()
    x15.selection.select(("ranges", None), " ", "@")
    x15.clear()
    x15.paste()
    ########
    ing15.selection.select(("ranges", None), "[", "`")
    ing15.copy()
    x15.selection.select(("ranges", None), "[", "`")
    x15.clear()
    x15.paste()
    ########
    ing15.selection.select(("ranges", None), "{", "~")
    ing15.copy()
    x15.selection.select(("ranges", None), "{", "~")
    x15.clear()
    x15.paste()
    ########
    ing15.selection.select(("ranges", None), "I", "S")
    ing15.copy()
    x15.selection.select(("ranges", None), "I", "S")
    x15.clear()
    x15.paste()
    ########
    ing15.selection.select(("ranges", None), "U", "Z")
    ing15.copy()
    x15.selection.select(("ranges", None), "U", "Z")
    x15.clear()
    x15.paste()
    ########        
    x15.save()
    ########    
    for simbl in ing2others_tpl15:
        ing15.selection.select(simbl)
        ing15.copy()
        x15.selection.select(simbl)
        x15.clear()
        x15.paste()
    ########        
    x15.save()
    x15.close()
ing15.close()
