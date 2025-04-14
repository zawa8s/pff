#!/usr/bin/python3
import fontforge
from uhin_dikt import asc_2_uhin_dikt
print(asc_2_uhin_dikt)
langscripts = (
    "ing",
    "hindi",
    "bangla","guzrati","gurmukhi","oriya",
    "korean",
    "telugu","tamil","kannada","malayalam","sinhala"
    # "binaryv"
)
##############
def asc_2_uhin(sfdroot,b_or_s,ftype,asc_2_uhin_dikt):
    sfddir=f"{sfdroot}/{b_or_s}/source{ftype}/"
    for lscript in langscripts:
        sfd_lscript = fontforge.open(f"{sfddir}/{lscript}{ftype}.sfd")
        print(f"lscript is {lscript} and sfd_lscript family name is {sfd_lscript.familyname}")
        for srclok, trglok in asc_2_uhin_dikt.items():
            sfd_lscript.selection.select(srclok)
            sfd_lscript.copyReference()
            sfd_lscript.selection.select(trglok)
            sfd_lscript.clear()
            sfd_lscript.paste()
        sfd_lscript.save()
        sfd_lscript.close()
##############
if __name__ == "__main__":
    sfdroot=f"/home/viml/mg/zw8/pff/sfd/"
    b_or_s = "big"
    ftype = "115b"
    asc_2_uhin(sfdroot,b_or_s,ftype,asc_2_uhin_dikt)

