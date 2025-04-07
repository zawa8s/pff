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
src15mbig = "/home/viml/mg/zw8/pff/sfd/big/source15mb/"
ing15mb = fontforge.open(f"{src15mbig}/ing15mb.sfd")
fromtotpl = (
    "o","a","A","H",
    # "i","j","o","q","u","v","w","x",
    # "C","E","G","H","I","J","O","Q","U","V","W","X",
    # "A","L","M","N","P","R","Y",
)
for lang in languages:
    f15mb = fontforge.open(f"{src15mbig}/{lang}15mb.sfd")
    print(f"language is {lang} and f15mb family name is {f15mb.familyname}")
    ###########
    for loc in fromtotpl:
        ing15mb.selection.select(loc)
        ing15mb.copy()
        f15mb.selection.select(loc)
        f15mb.clear()
        f15mb.paste()
    ###########
    f15mb.save()
    f15mb.close()
    ###########
ing15mb.close()