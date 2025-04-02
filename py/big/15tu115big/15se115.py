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
    x15.selection.select(("ranges", None), "!", "~")
    x15.copy()
    x115.selection.select(("ranges", None), "!", "~")
    x115.clear()
    x115.paste()
    x115.save()
    x115.close()
    x15.close()