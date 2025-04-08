#!/usr/bin/python3
import fontforge
############### "ing",
def ing_2_others(sfddir,b_or_s,ftype,tpl):
    src = f"{sfddir}/{b_or_s}/source{ftype}/"
    fing = fontforge.open(f"{src}/ing{ftype}.sfd")
    languages = (
        "hindi",
        "bangla","guzrati","gurmukhi","oriya",
        "korean",
        "telugu","tamil","kannada","malayalam","sinhala",
        "binaryw",
    )
    for lang in languages:
        flang = fontforge.open(f"{src}/{lang}{ftype}.sfd")
        print(f"lang is {lang} and flang family name is {flang.familyname}")
        ########
        for loc in tpl:
            fing.selection.select(loc)
            fing.copy()
            flang.selection.select(loc)
            flang.clear()
            flang.paste()
        ######## 
        flang.save()
        flang.close()
        ########        
    fing.close()
##############
if __name__ == "__main__":
    sfddir = "/home/viml/mg/zw8/pff/sfd/"
    b_or_s = "big"
    ftype = "15mb"  #"115b"
    tpl = ("a","A","v","V","x","X","j","J") # ("a","A","v","x","V","X",140,0x93E)
    ing_2_others(sfddir,b_or_s,ftype,tpl)