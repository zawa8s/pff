#!/usr/bin/python3
import fontforge
from hinu1_ing2others_115list import hinu1_ing2others_115tpl
print(hinu1_ing2others_115tpl)
langs = (
    # "ing",
    "hindi",
    "bangla","guzrati","gurmukhi","oriya",
    "korean",
    "telugu","tamil","kannada","malayalam","sinhala"
    # ,"eng","binaryv","binaryh","hex",
    # "notosans"
)
ing115 = fontforge.open(f"/home/viml/mg/zw8/pff/sfd/source115/ing115.sfd")
for l in langs:
    f115 = fontforge.open(f"/home/viml/mg/zw8/pff/sfd/source115/{l}115.sfd")
    print(f"language is {l} and f115 family name is {f115.familyname}")
    ########
    for simbl in hinu1_ing2others_115tpl:
        ing115.selection.select(simbl)
        ing115.copy()
        f115.selection.select(simbl)
        f115.clear()
        f115.paste()
    ########        
    f115.save()
    f115.close()
ing115.close()
