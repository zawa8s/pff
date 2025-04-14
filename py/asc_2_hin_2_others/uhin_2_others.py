#!/usr/bin/python3
import fontforge
# import sys
from uhin_dikt import uhin_dikt
print(uhin_dikt)
utftot = (
    ("cbindu", "cbindu", "nbindu", "colon",
     "_e", "X", "a", "_i", "_i", "_u", "_u", "ri", "l", "_e", "_e", "_e", "_e", "_o", "_o", "_o", "_o",
     "k", "K", "g", "G", "N", "c", "C", "z", "Z", "n", "t", "T", "d", "D", "n", "j", "J", "q", "Q", "n", "n",
     "p", "f", "b", "B", "m", "y", "r", "r", "l", "l", "l", "w", "S", "s", "s", "V",
     "e", "i", "nukta", "nukta",
     "a", "spesl", "i", "u", "u", "ri", "ri", "e", "e", "e", "e", "o", "o", "o", "o", "nukta",
     "null", "o", "om", "udatta", "anudtta", "`", "'", "e", "u", "u",
     "k", "K", "g", "z", "d", "D", "f", "y", "ri", "l", "l", "l", ".", ".",
     "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "hsdot",
     "X", "_e", "_o", "_o", "_u", "_u", "q", "Z", "y", "g", "z", "?", "d", "b",
    ),
    ("spesl", "cbindu", "nbindu", "colon",
     "_e", "X", "a", "_i", "_i", "_u", "_u", "ri", "l", "_e", "_e", "_e", "_e", "_o", "_o", "_o", "_o",
     "k", "K", "g", "G", "N", "c", "C", "z", "Z", "n", "t", "T", "d", "D", "n", "j", "J", "q", "Q", "n", "n",
     "p", "f", "b", "B", "m", "y", "r", "r", "l", "l", "l", "w", "S", "s", "s", "V",
     "null", "null", "nukta", "nukta",
     "a", "spesl", "i", "u", "u", "ri", "ri", "null", "null", "spesl", "spesl", "null", "null", "spesl", "spesl", "nukta", "j", "null", "null", "null", "null", "null", "null", "null", "null", "o", "null", "null", "null", "null", "d", "D", "null", "y", "ri", "l", "l", "l", ".", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "r", "w", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "nbindu", "-", "nukta", "null" ),
    ("cbindu", "cbindu", "nbindu", "colon",
     "_e", "X", "a", "_i", "_i", "_u", "_u", "ri", "l", "_e", "_e", "_e", "_e", "_o", "_o", "_o", "_o",
     "k", "K", "g", "G", "N", "c", "C", "z", "Z", "n", "t", "T", "d", "D", "n", "j", "J", "q", "Q", "n", "n",
     "p", "f", "b", "B", "m", "y", "r", "r", "l", "l", "l", "w", "S", "s", "s", "V",
     "null", "null", "nukta", "nukta",
     "a", "spesl", "i", "u", "u", "ri", "ri", "null", "null", "e", "e", "null", "null", "o", "o", "nukta",
     "null", "null", "null", "udatta", "null", "null", "null", "null", "null", "null", "null", "K", "g", "z", "d", "D", "f", "null", "ri", "l", "l", "l", ".", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "nbindu", "cbindu", "i", "u", "spesl", "y", "-", "null", "null", "null", "null", "null", "null", "null", "null", "null"),
    ("cbindu", "cbindu", "nbindu", "colon", "_e", "X", "a", "_i", "_i", "_u", "_u", "ri", "l", "_e", "_e", "_e", "_e", "_o", "_o", "_o", "_o", "k", "K", "g", "G", "N", "c", "C", "z", "Z", "n", "t", "T", "d", "D", "n", "j", "J", "q", "Q", "n", "n", "p", "f", "b", "B", "m", "y", "r", "r", "l", "l", "l", "w", "S", "s", "s", "V", "null", "null", "nukta", "nukta", "a", "spesl", "i", "u", "u", "ri", "ri", "e", "null", "e", "e", "o", "null", "o", "o", "nukta", "null", "null", "om", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "ri", "l", "l", "l", ".", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "r", "null", "null", "null", "null", "null", "null", "null", "Z", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl" ),
    ("cbindu", "cbindu", "nbindu", "colon", "_e", "X", "a", "_i", "_i", "_u", "_u", "ri", "l", "_e", "_e", "_e", "_e", "_o", "_o", "_o", "_o", "k", "K", "g", "G", "N", "c", "C", "z", "Z", "n", "t", "T", "d", "D", "n", "j", "J", "q", "Q", "n", "n", "p", "f", "b", "B", "m", "y", "r", "r", "l", "l", "l", "w", "S", "s", "s", "V", "null", "null", "nukta", "nukta", "a", "i", "i", "u", "u", "ri", "ri", "null", "null", "spesl", "spesl", "null", "null", "spesl", "spesl", "nukta", "null", "null", "null", "null", "null", "null", "null", "spesl", "e", "o", "null", "null", "null", "null", "r", "D", "null", "y", "ri", "l", "l", "l", ".", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "spesl", "w", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "null", "null", "null", "null", "null", "null", "null", "null"),
    ("null", "null", "nbindu", "colon", "_e", "X", "a", "_i", "_i", "_u", "_u", "ri", "l", "_e", "_e", "_e", "_e", "_o", "_o", "_o", "_o", "k", "K", "g", "G", "N", "c", "C", "z", "Z", "n", "t", "T", "d", "D", "n", "j", "J", "q", "Q", "n", "n", "p", "f", "b", "B", "m", "y", "r", "r", "l", "l", "l", "w", "S", "s", "s", "V", "null", "null", "nukta", "nukta", "a", "i", "i", "u", "u", "ri", "ri", "null", "spesl", "spesl", "spesl", "null", "spesl", "spesl", "spesl", "nukta", "null", "null", "om", "null", "null", "null", "null", "null", "null", "o", "null", "null", "null", "null", "null", "null", "null", "null", "ri", "l", "l", "l", ".", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "ten", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "null", "null", "null", "null", "null"),
    ("cbindu", "cbindu", "nbindu", "colon", "_e", "X", "a", "_i", "_i", "_u", "_u", "ri", "l", "_e", "_e", "_e", "_e", "_o", "_o", "_o", "_o", "k", "K", "g", "G", "N", "c", "C", "z", "Z", "n", "t", "T", "d", "D", "n", "j", "J", "q", "Q", "n", "n", "p", "f", "b", "B", "m", "y", "r", "r", "l", "l", "l", "w", "S", "s", "s", "V", "null", "null", "nukta", "nukta", "a", "i", "i", "u", "u", "ri", "ri", "null", "e", "e", "e", "null", "o", "o", "o", "nukta", "null", "null", "null", "null", "null", "null", "null", "o", "e", "null", "s", "z", "r", "null", "null", "n", "null", "null", "ri", "l", "l", "l", ".", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "null", "null", "null", "null", "null", "null", "null", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl"),
    ("cbindu", "cbindu", "nbindu", "colon", "_e", "X", "a", "_i", "_i", "_u", "_u", "ri", "l", "_e", "_e", "_e", "_e", "_o", "_o", "_o", "_o", "k", "K", "g", "G", "N", "c", "C", "z", "Z", "n", "t", "T", "d", "D", "n", "j", "J", "q", "Q", "n", "n", "p", "f", "b", "B", "m", "y", "r", "r", "l", "l", "l", "w", "S", "s", "s", "V", "null", "null", "nukta", "nukta", "a", "i", "i", "u", "u", "ri", "ri", "null", "e", "e", "e", "null", "o", "o", "o", "nukta", "null", "null", "null", "null", "null", "null", "null", "spesl", "spesl", "null", "null", "null", "null", "null", "null", "n", "l", "null", "ri", "l", "l", "l", ".", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "ten", "spesl", "spesl", "spesl", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null"),
    ("cbindu", "cbindu", "nbindu", "colon", "_e", "X", "a", "_i", "_i", "_u", "_u", "ri", "l", "_e", "_e", "_e", "_e", "_o", "_o", "_o", "_o", "k", "K", "g", "G", "N", "c", "C", "z", "Z", "n", "t", "T", "d", "D", "n", "j", "J", "q", "Q", "n", "n", "p", "f", "b", "B", "m", "y", "r", "r", "l", "l", "l", "w", "S", "s", "s", "V", "spesl", "cbindu", "nukta", "spesl", "a", "i", "i", "u", "u", "ri", "ri", "null", "spesl", "spesl", "spesl", "null", "spesl", "spesl", "spesl", "nukta", "cbindu", "o", "null", "null", "null", "null", "m", "y", "l", "o", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "ri", "l", "l", "l", ".", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "n", "n", "r", "l", "l", "k"),
    ("null", "cbindu", "nbindu", "colon", "null", 
    "X", "a", "Ae", "ae", "_i", "_i", "_u", "_u", "r", "ri", "l", "l", "_e", "_e", "_e", "o", "o", "o", 
    "null", "null", "null", 
    "k", "K", "g", "G", "N", "N", 
    "c", "C", "z", "Z", "n", "n", "n", 
    "t", "T", "d", "D", "n", "n", "t", "T", "d", "D", "n",
    "null", "n", 
    "p", "f", "b", "B", "m", "mb", "y", "r", "null", "l", "null", "null",
    "w", "S", "s", "s", "V", "l", "f",
    "null", "null", "null", "nukta", "null", "null", "null", "null",
    "a", "e", "ae", "i", "i", "u", "null", "u", "null", "ri", "e", "e", "e", "o", "o", "o", "l",
    "null", "null", "null", "null", "null", "null",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "null", "null",
    "ri", "l", "spesl", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null")
)
# for langi in range(len(utftot)):
#     print(f"langi is {langi} . len(utftot[{langi}]) is {len(utftot[langi])}")
# exit()
langscripts = (
    "ing",
    "hindi",
    "bangla","guzrati","gurmukhi","oriya",
    "korean",
    "telugu","tamil","kannada","malayalam","sinhala"
    # ,"eng","binaryv","binaryh","hex",
    # "notosans"
)
################
def uhin_2_others(sfdroot,b_or_s,ftype):
    sfddir = f"{sfdroot}/{b_or_s}/source{ftype}/"
    for lscript in langscripts:
        startpoint = 0x900
        sfd_lscript = fontforge.open(f"{sfddir}/{lscript}{ftype}.sfd")
        print(f"lscript is {lscript} and sfd_lscript family name is {sfd_lscript.familyname}")
        for langi in range(10): #(len(utftot)):
            for remainder_i in range(128): #(len(utftot[langi])):
                trglok = startpoint + 128*langi + remainder_i
                print(f"langi is {langi} . remainder_i is {remainder_i} and target_i is {trglok}")
                utf_glyph_name = utftot[langi][remainder_i]
                if utf_glyph_name in uhin_dikt:
                    srclok = uhin_dikt[utf_glyph_name]
                    print(f"utf_glyph_name is {utf_glyph_name} and srclok is {srclok} and trglok is {trglok}")
                    if srclok != trglok:
                        print(f"{srclok} not ekual to {trglok}")
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
    uhin_2_others(sfdroot,b_or_s,ftype)
