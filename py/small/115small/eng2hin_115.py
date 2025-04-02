#!/usr/bin/python3
import fontforge
from eng2hin_dict_115 import eng2hindict
print(eng2hindict)
langs = (
    "ing",
    "hindi",
    "bangla","guzrati","gurmukhi","oriya",
    "korean",
    "telugu","tamil","kannada","malayalam","sinhala"
    # "binaryv"
)
for l in langs:
    f115 = fontforge.open(f"/home/viml/mg/zw8/pff/sfd/source115/{l}115.sfd")
    print(f"language is {l} and f115 family name is {f115.familyname}")
    for engsim, hinditarget in eng2hindict.items():
        f115.selection.select(engsim)
        f115.copyReference()
        f115.selection.select(hinditarget)
        f115.clear()
        f115.paste()
    f115.save()
    f115.close()
