#!/usr/bin/python3
import fontforge
from notolists15b import noto_remaindermap_dikt15b 
from notolists15b import notosinhala_remaindermap_dikt15b 
from language_lists import lang_index_dikt
# langs = (
#     # "ing",
#     # "hindi",
#     "bangla","guzrati","gurmukhi","oriya",
#     # "korean",
#     "telugu","kannada","malayalam",
#     "tamil",
#     # "sinhala",
#     # ,"eng","binaryw","binaryh","hex",
#     # "notosans"
# )

# for lang in langs:
#     fnoto = fontforge.open(f"/home/viml/mg/zw8/pff/sfd/b/source15b/noto/noto{lang}.sfd")
#     f15b = fontforge.open(f"/home/viml/mg/zw8/pff/sfd/b/source15b/{lang}15b.sfd")
#     print(f"lang is {lang} and f15b family name is {f15b.familyname}")
#     ########
#     startpoint = 0x900
#     for (trg,srcremainder) in noto_remaindermap_dikt15b.items():
#         src = startpoint + lang_index_dikt[lang]*0x80 + srcremainder
#         fnoto.selection.select(src)
#         fnoto.copy()
#         f15b.selection.select(trg)
#         f15b.clear()
#         f15b.paste()
#     f15b.save()
#     f15b.close()
#     fnoto.close()

#seperately for sinhala
#######################
langs = ("sinhala",)
startpoint = 0x900
for lang in langs:
    fnoto = fontforge.open(f"/home/viml/mg/zw8/pff/sfd/b/source15b/noto/noto{lang}.sfd")
    f15b = fontforge.open(f"/home/viml/mg/zw8/pff/sfd/b/source15b/{lang}15b.sfd")
    print(f"lang is {lang} and f15b family name is {f15b.familyname}")
    ########
    for (trg,srcremainder) in notosinhala_remaindermap_dikt15b.items():
        src = startpoint + lang_index_dikt[lang]*0x80 + srcremainder
        fnoto.selection.select(src)
        fnoto.copy()
        f15b.selection.select(trg)
        f15b.clear()
        f15b.paste()
    f15b.save()
    f15b.close()
    fnoto.close()
