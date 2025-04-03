#!/usr/bin/python3
import fontforge
# import sys
from merged_dikt_115big import merged_dikt_115big
print(merged_dikt_115big)
utftot = (
    ("cbindu", "cbindu", "nbindu", "colon",
     "_e", "X", "aa", "_i", "_i", "_u", "_u", "ri", "l", "_e", "_e", "_e", "_e", "_o", "_o", "_o", "_o",
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
     "_e", "X", "aa", "_i", "_i", "_u", "_u", "ri", "l", "_e", "_e", "_e", "_e", "_o", "_o", "_o", "_o",
     "k", "K", "g", "G", "N", "c", "C", "z", "Z", "n", "t", "T", "d", "D", "n", "j", "J", "q", "Q", "n", "n",
     "p", "f", "b", "B", "m", "y", "r", "r", "l", "l", "l", "w", "S", "s", "s", "V",
     "null", "null", "nukta", "nukta",
     "a", "spesl", "i", "u", "u", "ri", "ri", "null", "null", "spesl", "spesl", "null", "null", "spesl", "spesl", "nukta", "j", "null", "null", "null", "null", "null", "null", "null", "null", "o", "null", "null", "null", "null", "d", "D", "null", "y", "ri", "l", "l", "l", ".", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "r", "w", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "nbindu", "-", "nukta", "null" ),
    ("cbindu", "cbindu", "nbindu", "colon",
     "_e", "X", "aa", "_i", "_i", "_u", "_u", "ri", "l", "_e", "_e", "_e", "_e", "_o", "_o", "_o", "_o",
     "k", "K", "g", "G", "N", "c", "C", "z", "Z", "n", "t", "T", "d", "D", "n", "j", "J", "q", "Q", "n", "n",
     "p", "f", "b", "B", "m", "y", "r", "r", "l", "l", "l", "w", "S", "s", "s", "V",
     "null", "null", "nukta", "nukta",
     "a", "spesl", "i", "u", "u", "ri", "ri", "null", "null", "e", "e", "null", "null", "o", "o", "nukta",
     "null", "null", "null", "udatta", "null", "null", "null", "null", "null", "null", "null", "K", "g", "z", "d", "D", "f", "null", "ri", "l", "l", "l", ".", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "nbindu", "cbindu", "i", "u", "spesl", "y", "-", "null", "null", "null", "null", "null", "null", "null", "null", "null"),
    ("cbindu", "cbindu", "nbindu", "colon", "_e", "X", "aa", "_i", "_i", "_u", "_u", "ri", "l", "_e", "_e", "_e", "_e", "_o", "_o", "_o", "_o", "k", "K", "g", "G", "N", "c", "C", "z", "Z", "n", "t", "T", "d", "D", "n", "j", "J", "q", "Q", "n", "n", "p", "f", "b", "B", "m", "y", "r", "r", "l", "l", "l", "w", "S", "s", "s", "V", "null", "null", "nukta", "nukta", "a", "spesl", "i", "u", "u", "ri", "ri", "e", "null", "e", "e", "o", "null", "o", "o", "nukta", "null", "null", "om", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "ri", "l", "l", "l", ".", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "r", "null", "null", "null", "null", "null", "null", "null", "Z", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl" ),
    ("cbindu", "cbindu", "nbindu", "colon", "_e", "X", "aa", "_i", "_i", "_u", "_u", "ri", "l", "_e", "_e", "_e", "_e", "_o", "_o", "_o", "_o", "k", "K", "g", "G", "N", "c", "C", "z", "Z", "n", "t", "T", "d", "D", "n", "j", "J", "q", "Q", "n", "n", "p", "f", "b", "B", "m", "y", "r", "r", "l", "l", "l", "w", "S", "s", "s", "V", "null", "null", "nukta", "nukta", "a", "i", "i", "u", "u", "ri", "ri", "null", "null", "spesl", "spesl", "null", "null", "spesl", "spesl", "nukta", "null", "null", "null", "null", "null", "null", "null", "spesl", "e", "o", "null", "null", "null", "null", "r", "D", "null", "y", "ri", "l", "l", "l", ".", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "spesl", "w", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "null", "null", "null", "null", "null", "null", "null", "null"),
    ("null", "null", "nbindu", "colon", "_e", "X", "aa", "_i", "_i", "_u", "_u", "ri", "l", "_e", "_e", "_e", "_e", "_o", "_o", "_o", "_o", "k", "K", "g", "G", "N", "c", "C", "z", "Z", "n", "t", "T", "d", "D", "n", "j", "J", "q", "Q", "n", "n", "p", "f", "b", "B", "m", "y", "r", "r", "l", "l", "l", "w", "S", "s", "s", "V", "null", "null", "nukta", "nukta", "a", "i", "i", "u", "u", "ri", "ri", "null", "spesl", "spesl", "spesl", "null", "spesl", "spesl", "spesl", "nukta", "null", "null", "om", "null", "null", "null", "null", "null", "null", "o", "null", "null", "null", "null", "null", "null", "null", "null", "ri", "l", "l", "l", ".", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "ten", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "null", "null", "null", "null", "null"),
    ("cbindu", "cbindu", "nbindu", "colon", "_e", "X", "aa", "_i", "_i", "_u", "_u", "ri", "l", "_e", "_e", "_e", "_e", "_o", "_o", "_o", "_o", "k", "K", "g", "G", "N", "c", "C", "z", "Z", "n", "t", "T", "d", "D", "n", "j", "J", "q", "Q", "n", "n", "p", "f", "b", "B", "m", "y", "r", "r", "l", "l", "l", "w", "S", "s", "s", "V", "null", "null", "nukta", "nukta", "a", "i", "i", "u", "u", "ri", "ri", "null", "e", "e", "e", "null", "o", "o", "o", "nukta", "null", "null", "null", "null", "null", "null", "null", "o", "e", "null", "s", "z", "r", "null", "null", "n", "null", "null", "ri", "l", "l", "l", ".", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "null", "null", "null", "null", "null", "null", "null", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl"),
    ("cbindu", "cbindu", "nbindu", "colon", "_e", "X", "aa", "_i", "_i", "_u", "_u", "ri", "l", "_e", "_e", "_e", "_e", "_o", "_o", "_o", "_o", "k", "K", "g", "G", "N", "c", "C", "z", "Z", "n", "t", "T", "d", "D", "n", "j", "J", "q", "Q", "n", "n", "p", "f", "b", "B", "m", "y", "r", "r", "l", "l", "l", "w", "S", "s", "s", "V", "null", "null", "nukta", "nukta", "a", "i", "i", "u", "u", "ri", "ri", "null", "e", "e", "e", "null", "o", "o", "o", "nukta", "null", "null", "null", "null", "null", "null", "null", "spesl", "spesl", "null", "null", "null", "null", "null", "null", "n", "l", "null", "ri", "l", "l", "l", ".", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "ten", "spesl", "spesl", "spesl", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null"),
    ("cbindu", "cbindu", "nbindu", "colon", "_e", "X", "aa", "_i", "_i", "_u", "_u", "ri", "l", "_e", "_e", "_e", "_e", "_o", "_o", "_o", "_o", "k", "K", "g", "G", "N", "c", "C", "z", "Z", "n", "t", "T", "d", "D", "n", "j", "J", "q", "Q", "n", "n", "p", "f", "b", "B", "m", "y", "r", "r", "l", "l", "l", "w", "S", "s", "s", "V", "spesl", "cbindu", "nukta", "spesl", "a", "i", "i", "u", "u", "ri", "ri", "null", "spesl", "spesl", "spesl", "null", "spesl", "spesl", "spesl", "nukta", "cbindu", "o", "null", "null", "null", "null", "m", "y", "l", "o", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "ri", "l", "l", "l", ".", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "spesl", "n", "n", "r", "l", "l", "k"),
    ("null", "cbindu", "nbindu", "colon", "null", 
    "X", "aa", "Ae", "ae", "_i", "_i", "_u", "_u", "r", "ri", "l", "l", "_e", "_e", "_e", "o", "o", "o", 
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
startpoint = 0x900
scripts = (
    "ing",
    "hindi",
    "bangla","guzrati","gurmukhi","oriya",
    "korean",
    "telugu","tamil","kannada","malayalam","sinhala"
    # ,"eng","binaryv","binaryh","hex",
    # "notosans"
)
pffdir="/home/viml/mg/zw8/pff/"
src115big=f"{pffdir}/sfd/big/source115b/"
for x in scripts:
    f115big = fontforge.open(f"{src115big}/{x}115b.sfd")
    print(f"x is {x} and f115big family name is {f115big.familyname}")
    for langi in range(10): #(len(utftot)):
        for remainder_i in range(128): #(len(utftot[langi])):
            target_i = startpoint + 128*langi + remainder_i
            print(f"langi is {langi} . remainder_i is {remainder_i} and target_i is {target_i}")
            src_simbl = utftot[langi][remainder_i]
            if src_simbl in merged_dikt_115big:
                src_simbl_i = merged_dikt_115big[src_simbl]
                print(f"src_simbl is {src_simbl} and src_simbl_i is {src_simbl_i} and target_i is {target_i}")
                if src_simbl_i != target_i:
                    f115big.selection.select(src_simbl_i)
                    f115big.copyReference()
                    f115big.selection.select(target_i)
                    f115big.clear()
                    f115big.paste()
    f115big.save()
    f115big.close()

