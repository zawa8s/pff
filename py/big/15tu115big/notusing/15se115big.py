#!/usr/bin/python3
import fontforge
languages = (
    "ing",
    "hindi",
    "bangla","guzrati","gurmukhi","oriya",
    "korean",
    "telugu","tamil","kannada","malayalam","sinhala"
    # ,"eng","binaryv","binaryh","hex",
    # "notosans"
)
src15big = "/home/viml/mg/zw8/pff/sfd/big/source15b/"
src115big = "/home/viml/mg/zw8/pff/sfd/big/source115b/"
for lang in languages:
    font15big = fontforge.open(f"{src15big}/{lang}15b.sfd")
    font115big = fontforge.open(f"{src115big}/{lang}115b.sfd")
    print(f"lang is {lang} and font15big family name is {font15big.familyname} and font115big family name is {font115big.familyname}")
    font15big.selection.select(("ranges", None), " ", 159)
    font15big.copy()
    font115big.selection.select(("ranges", None), " ", 159)
    font115big.clear()
    font115big.paste()
    font115big.save()
    font115big.close()
    font15big.close()