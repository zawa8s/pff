#!/usr/bin/python3
import fontforge

scripts = (
    "ing",
    "hindi",
    "bangla","guzrati","gurmukhi","oriya",
    "korean",
    "telugu","tamil","kannada","malayalam","sinhala"
    # ,"eng","binaryv","binaryh","hex",
    # "notosans"
)
src15b = "/home/viml/mg/zw8/pff/sfd/big/source15b/"
src115b = "/home/viml/mg/zw8/pff/sfd/big/source115b/"
ing15b = fontforge.open(f"{src15b}/ing15b.sfd")
for ls in scripts:
    f115b = fontforge.open(f"{src115b}/{ls}115b.sfd")
    print(f"langscript is {ls} and f115b family name is {f115b.familyname}")
    ########
    ing15b.selection.select("g")
    ing15b.copy()
    f115b.selection.select("g")
    f115b.clear()
    f115b.paste()
    ########        
    ing15b.selection.select("G")
    ing15b.copy()
    f115b.selection.select("G")
    f115b.clear()
    f115b.paste()
    ########        
    f115b.save()
    f115b.close()
ing15b.close()
