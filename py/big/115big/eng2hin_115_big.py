#!/usr/bin/python3
import fontforge
from eng2hin_dict_115_big import eng2hin_dict_115_big
print(eng2hin_dict_115_big)
languages = (
    "ing",
    "hindi",
    "bangla","guzrati","gurmukhi","oriya",
    "korean",
    "telugu","tamil","kannada","malayalam","sinhala"
    # "binaryv"
)
pffdir="/home/viml/mg/zw8/pff/"
src115big=f"{pffdir}/sfd/big/source115b/"
for lang in languages:
    f115big = fontforge.open(f"{src115big}/{lang}115b.sfd")
    print(f"lang is {lang} and f115big family name is {f115big.familyname}")
    for engsim, hinditarget in eng2hin_dict_115_big.items():
        f115big.selection.select(engsim)
        f115big.copyReference()
        f115big.selection.select(hinditarget)
        f115big.clear()
        f115big.paste()
    f115big.save()
    f115big.close()
