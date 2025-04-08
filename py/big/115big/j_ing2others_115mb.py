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
src115b = "/home/viml/mg/zw8/pff/sfd/big/source115b/"
ing115b = fontforge.open(f"{src115b}/ing115b.sfd")
for lang in languages:
    f115b = fontforge.open(f"{src115b}/{lang}115b.sfd")
    print(f"lang is {lang} and f115b family name is {f115b.familyname}")
    ########
    ing115b.selection.select("j")
    ing115b.copy()
    f115b.selection.select("j")
    f115b.clear()
    f115b.paste()
    ######## 
    f115b.save()
    f115b.close()
    ########        
ing115b.close()
