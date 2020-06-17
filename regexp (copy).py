#!/usr/bin/python3

import re

regg2 = re.compile(r'\d+')

print("Enter your phone number")

regg = input()

regSearch = regg2.findall(regg)


for ree in regSearch:
    if len(ree) >= 10 and len(ree) < 12:
        if ree[:4] != "+234" and ree[0] != "0":
            reesplited = ree.split()
            reesplited.append("+234")
            reesplited.sort(reverse=False)
            joineds = ''.join(reesplited)
            print(joineds)
        elif ree[:4] != "+234" and ree[0] == "0":
            
            remzero = ree.strip(ree[0])
            reesplited = remzero.split()
            reesplited.append("+234")
            reesplited.sort(reverse=False)
            joinremzero = ''.join(reesplited)
            print(joinremzero)
    elif len(ree) > 12:
        print("Your phone number " + ree + " is more than expected")
    else:
        print("Your phone number " + ree + " is less than expected")
