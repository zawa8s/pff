#!/usr/bin/python3
import fontforge
languages = (
    # "ing",
    "hindi",
    "bangla","guzrati","gurmukhi","oriya",
    "korean",
    "telugu",
    "tamil",
    "kannada","malayalam","sinhala"
    # ,"eng","binaryv","binaryh","hex",
    # "notosans"
)
kztdbs_dot_dikt={
    "k" : "K", "z" : "Z", "t" : "T", "d" : "D", "b" : "B", "s" : "S",
}
src15big = "/home/viml/mg/zw8/pff/sfd/big/source15b/"
# src115big = "/home/viml/mg/zw8/pff/sfd/big/source115b/"
for lang in languages:
    font15big = fontforge.open(f"{src15big}/{lang}15b.sfd")
    print(f"lang is {lang} and font15big family name is {font15big.familyname}")
    for (srclok,trglok) in kztdbs_dot_dikt.items():
        font15big.selection.select(srclok)
        font15big.copyReference()
        font15big.selection.select(trglok)
        font15big.clear()
        font15big.paste()
    font15big.save()
    font15big.close()