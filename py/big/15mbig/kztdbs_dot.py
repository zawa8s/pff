#!/usr/bin/python3
import fontforge
languages = (
    # "ing",
    "hindi",
    "bangla","guzrati","gurmukhi","oriya",
    # "korean",
    "telugu",
    "tamil",
    "kannada","malayalam","sinhala"
    # ,"eng","binaryv","binaryh","hex",
    # "notosans"
)
kztdbs_dot_dikt={
    "k" : "K", "z" : "Z", "t" : "T", "d" : "D", "b" : "B", "s" : "S", "j" : "J", "q" : "Q",
}
src15mbig = "/home/viml/mg/zw8/pff/sfd/big/source15mb/"
for lang in languages:
    font15mbig = fontforge.open(f"{src15mbig}/{lang}15mb.sfd")
    print(f"lang is {lang} and font15mbig family name is {font15mbig.familyname}")
    for (srclok,trglok) in kztdbs_dot_dikt.items():
        font15mbig.selection.select(srclok)
        font15mbig.copyReference()
        font15mbig.selection.select(trglok)
        font15mbig.clear()
        font15mbig.paste()
    font15mbig.save()
    font15mbig.close()