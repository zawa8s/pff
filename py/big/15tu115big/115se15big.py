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
for x in scripts:
    x15 = fontforge.open(f"/home/viml/mg/zw8/pff/sfd/source15/{x}15.sfd")
    x115 = fontforge.open(f"/home/viml/mg/zw8/pff/sfd/source115/{x}115.sfd")
    print(f"x is {x} and x15 family name is {x15.familyname} and x115 family name is {x115.familyname}")
    x115.selection.select(("ranges", None), "!", "~")
    x115.copy()
    x15.selection.select(("ranges", None), "!", "~")
    x15.clear()
    x15.paste()
    x15.save()
    x15.close()
    x115.close()