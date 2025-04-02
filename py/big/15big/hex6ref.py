#!/usr/bin/python3
import fontforge
langs = (
    "ing",
    "hindi",
    "bangla","guzrati","gurmukhi","oriya",
    "korean",
    "telugu","tamil","kannada","malayalam","sinhala"
    # ,"eng","binaryw","binaryh","hex",
    # "notosans"
)
# binaryw15bf = fontforge.open(f"/home/viml/mg/zw8/pff/sfd/b/source15b/binaryw15b.sfd")
for l in langs:
    # f15s = fontforge.open(f"/home/viml/mg/zw8/pff/sfd/s/source15s/{l}15s.sfd")
    f15b = fontforge.open(f"/home/viml/mg/zw8/pff/sfd/b/source15b/{l}15b.sfd")
    print(f"lang is {l} and f15b family name is {f15b.familyname}")
    ########
    # ing15.selection.select(("ranges", None), " ", "@")
    # ing15.copy()
    # x15.selection.select(("ranges", None), " ", "@")
    # x15.clear()
    # x15.paste()    
    ######## 
    dikt = {138:"L", 139:"Y", 140:"v", 141:"W", 142:"P", 143:"F",}
    for (trg,src) in dikt.items():
        # binaryw15bf.selection.select(src)
        # binaryw15bf.copy()
        f15b.selection.select(src)
        f15b.copyReference()
        f15b.selection.select(trg)
        f15b.clear()
        f15b.paste()
    f15b.save()
    f15b.close()
    ########   
    # tpl = (
    #     "b", "d", "f", "k", "l", "m", "n", "p", "r", "s", "t", "y", "z"
    # ) 
    # for simbl in tpl:
    #     f15s.selection.select(simbl)
    #     f15s.copy()
    #     f15b.selection.select(simbl)
    #     f15b.clear()
    #     f15b.paste()
    ########        
        # f15b.save()
        # f15b.close()
    # f15s.close()
    ########        
# binaryw15bf.close()
