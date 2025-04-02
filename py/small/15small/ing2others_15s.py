#!/usr/bin/python3
import fontforge
#from 115 import eng2hinsimblsdict
from ing2others_dict15s import ing2others_tpl15s
print(ing2others_tpl15s)
langs = (
    # "ing",
    "hindi",
    "bangla","guzrati","gurmukhi","oriya",
    "korean",
    "telugu","tamil","kannada","malayalam","sinhala"
    # ,"eng","binaryv","binaryh","hex",
    # "notosans"
)
ing15s = fontforge.open(f"/home/viml/mg/zw8/pff/sfd/s/source15s/ing15s.sfd")
for l in langs:
    f15s = fontforge.open(f"/home/viml/mg/zw8/pff/sfd/s/source15s/{l}15s.sfd")
    print(f"language is {l} and f15s family name is {f15s.familyname}")
    ########
    ing15s.selection.select(("ranges", None), " ", "@")
    ing15s.copy()
    f15s.selection.select(("ranges", None), " ", "@")
    f15s.clear()
    f15s.paste()
    ########
    ing15s.selection.select(("ranges", None), "[", "`")
    ing15s.copy()
    f15s.selection.select(("ranges", None), "[", "`")
    f15s.clear()
    f15s.paste()
    ########
    ing15s.selection.select(("ranges", None), "{", "~")
    ing15s.copy()
    f15s.selection.select(("ranges", None), "{", "~")
    f15s.clear()
    f15s.paste()
    ########
    ing15s.selection.select(("ranges", None), "I", "S")
    ing15s.copy()
    f15s.selection.select(("ranges", None), "I", "S")
    f15s.clear()
    f15s.paste()
    ########
    ing15s.selection.select(("ranges", None), "U", "Z")
    ing15s.copy()
    f15s.selection.select(("ranges", None), "U", "Z")
    f15s.clear()
    f15s.paste()
    ########        
    f15s.save()
    ########    
    for simbl in ing2others_tpl15s:
        ing15s.selection.select(simbl)
        ing15s.copy()
        f15s.selection.select(simbl)
        f15s.clear()
        f15s.paste()
    ########        
    f15s.save()
    f15s.close()
ing15s.close()
