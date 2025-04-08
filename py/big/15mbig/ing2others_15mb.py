#!/usr/bin/python3
import fontforge

languages = (
    # "ing",
    "hindi",
    "bangla","guzrati","gurmukhi","oriya",
    "korean",
    "telugu","tamil","kannada","malayalam","sinhala"
    # ,"eng","binaryv","binaryh","hex",
    # "notosans"
)
src15mb = "/home/viml/mg/zw8/pff/sfd/big/source15mb/"
ing15mb = fontforge.open(f"{src15mb}/ing15mb.sfd")
for lang in languages:
    f15mb = fontforge.open(f"{src15mb}/{lang}15mb.sfd")
    print(f"lang is {lang} and f15mb family name is {f15mb.familyname}")
    ########
    ing15mb.selection.select("j")
    ing15mb.copy()
    f15mb.selection.select("j")
    f15mb.clear()
    f15mb.paste()
    ######## 
    f15mb.save()
    f15mb.close()
    ########        
ing15mb.close()
