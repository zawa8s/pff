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
for lang in languages:
    f15mb = fontforge.open(f"{src15mbig}/{lang}15mb.sfd")
    print(f"language is {lang} and f15mb family name is {f15mb.familyname}")
    ###########
    ing15mb.selection.select(("ranges", None), " ", "A")
    ing15mb.copy()
    f15mb.selection.select(("ranges", None), " ", "A")
    f15mb.clear()
    f15mb.paste()
    f15mb.save()
    ###########
    ing15mb.selection.select(("ranges", None), "[", "a")
    ing15mb.copy()
    f15mb.selection.select(("ranges", None), "[", "a")
    f15mb.clear()
    f15mb.paste()
    ###########
    ing15mb.selection.select(("ranges", None), "{", "~")
    ing15mb.copy()
    f15mb.selection.select(("ranges", None), "{", "~")
    f15mb.clear()
    f15mb.paste()
    ###########    
    fromtotpl = (
        "c","e","g","h","i","j","o","q","u","v","w","x",
        "C","E","G","H","I","J","O","Q","U","V","W","X",
        "A","L","M","N","P","R","Y",
    )
    for loc in fromtotpl:
        ing15mb.selection.select(loc)
        ing15mb.copy()
        f15mb.selection.select(loc)
        f15mb.clear()
        f15mb.paste()
    f15mb.save()
    ###########
    f15mb.save()
    f15mb.close()
    ###########
ing15mb.close()