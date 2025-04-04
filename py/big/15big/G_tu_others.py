#!/usr/bin/python3
import fontforge

scripts = (
    # "ing",
    "hindi",
    "bangla","guzrati","gurmukhi","oriya",
    "korean",
    "telugu","tamil","kannada","malayalam","sinhala"
    # ,"eng","binaryv","binaryh","hex",
    # "notosans"
)
src15b = "/home/viml/mg/zw8/pff/sfd/big/source15b/"
ing15b = fontforge.open(f"{src15b}/ing15b.sfd")
for ls in scripts:
    f15b = fontforge.open(f"{src15b}/{ls}15b.sfd")
    print(f"langscript is {ls} and f15b family name is {f15b.familyname}")
    ########
    ing15b.selection.select("g")
    ing15b.copy()
    f15b.selection.select("g")
    f15b.clear()
    f15b.paste()
    ########        
    ing15b.selection.select("G")
    ing15b.copy()
    f15b.selection.select("G")
    f15b.clear()
    f15b.paste()
    ########        
    f15b.save()
    f15b.close()
ing15b.close()
