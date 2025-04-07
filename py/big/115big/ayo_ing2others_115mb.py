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
src115big = "/home/viml/mg/zw8/pff/sfd/big/source115b/"
ing115b = fontforge.open(f"{src115big}/ing115b.sfd")
fromtotpl = (
    "a","A","H","o",
    # "i","j","o","q","u","v","w","x",
    # "C","E","G","H","I","J","O","Q","U","V","W","X",
    # "A","L","M","N","P","R","Y",
)
for lang in languages:
    f115b = fontforge.open(f"{src115big}/{lang}115b.sfd")
    print(f"language is {lang} and f115b family name is {f115b.familyname}")
    ###########
    for loc in fromtotpl:
        ing115b.selection.select(loc)
        ing115b.copy()
        f115b.selection.select(loc)
        f115b.clear()
        f115b.paste()
    ###########
    f115b.save()
    f115b.close()
    ###########
ing115b.close()