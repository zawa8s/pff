#!/usr/bin/python3
import fontforge
langs = (
    # "ing",
    # "hindi",
    "bangla","guzrati","gurmukhi","oriya",
    "korean",
    "telugu","tamil","kannada","malayalam","sinhala"
    # ,"eng","binaryv","binaryh","hex",
    # "notosans"
)
hindi15m = fontforge.open(f"/home/viml/mg/zw8/pff/sfd/source15m/hindi15m.sfd")
for l in langs:
    f15m = fontforge.open(f"/home/viml/mg/zw8/pff/sfd/source15m/{l}15m.sfd")
    print(f"language is {l} and f15m family name is {f15m.familyname}")
    ###########
    f15m.selection.select(("ranges", None), "b", "z")
    f15m.copy()
    f15m.selection.select(("ranges", None), 135, 159)
    f15m.clear()
    f15m.paste()
    f15m.save()
    ###########
    hindi15m.selection.select(("ranges", None), " ", "~")
    hindi15m.copy()
    f15m.selection.select(("ranges", None), " ", "~")
    f15m.clear()
    f15m.paste()
    ###########
    fromtodict = {
        135:"b", 137:"d", 139:"f", 144:"k", 145:"l", 146:"m", 147:"n",
        149:"p", 151:"r", 152:"s", 153:"t", 158:"y", 159:"z",
    }
    for (fromm, tuu) in fromtodict.items():
        print(f"fromm is {fromm} and tuu is {tuu}")
        f15m.selection.select(fromm)
        f15m.copy()
        f15m.selection.select(tuu)
        f15m.clear()
        f15m.paste()
    f15m.save()
    ###########
    f15m.save()
    f15m.close()
    ###########
hindi15m.close()