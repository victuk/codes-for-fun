#!/usr/bin/python3
import re

def rearrangedString(rearrange):
    theRegex = re.compile(r'[abcdefghijklmnopqrstuvwxyz]', re.I)
    strInRearrange = theRegex.findall(rearrange)
    strInRearrange.reverse()
    finalString =''.join(strInRearrange)
    return finalString

print(rearrangedString("8o*l=l++e9H"))
