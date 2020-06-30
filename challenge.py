#!/usr/bin/python3
import re

def rearrangedString(rearrange):
    theRegex = re.compile(r'[abcdefghijklmnopqrstuvwxyz\s]', re.I)
    strInRearrange = theRegex.findall(rearrange)
    strInRearrange.reverse()
    finalString =''.join(strInRearrange)
    return finalString

print(rearrangedString("234d%%%**&l#$%r@o))9((W 8o*l=l++e9H"))
