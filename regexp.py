#!/usr/bin/python3

import re

regg2 = re.compile(r'\d+')

print("Enter your phone number")

regg = "+2348137249484, -2348137249484, 08137249484, then 8137249484, \
 67875, 7898567864568, 7829384792387478329734"

regSearch = regg2.findall(regg)

print("=" * 50)

print("Your inputs are \n" + str(', \n'.join(regSearch)))

print("=" * 50)

print("Your outputs are as follows: ")

for ree in regSearch:
    if len(ree) >= 10 and len(ree) < 12:
        if ree[:4] != "234" and ree[0] != "0":
            reesplited = ree.split()
            reesplited.append("+234")
            reesplited.sort(reverse=False)
            joineds = ''.join(reesplited)
            print(ree + " has been converted to " + joineds + ".")
        elif ree[:4] != "234" and ree[0] == "0":
            
            remzero = ree.strip(ree[0])
            reesplited = remzero.split()
            reesplited.append("+234")
            reesplited.sort(reverse=False)
            joinremzero = ''.join(reesplited)
            print(ree + " has been converted to " + joinremzero + ".")
    elif ree[:3] == "234" and len(ree) == 13:
        reesplited = ree.split()
        reesplited.append("+")
        reesplited.sort(reverse=False)
        joinremzero = ''.join(reesplited)
        print(ree + " has been converted to " + joinremzero + ".")
    elif ree[:3] != "234" and len(ree) == 13:
        print("Your input " + ree + " is not correct. Your number should start with \"+234.\"")
    elif len(ree) > 13:
        print("Your phone number " + ree + " is more than expected. You input " + str(len(ree)) + " numbers.")
    else:
        print("Your phone number " + ree + " is less than expected. You input " + str(len(ree)) + " numbers.")
print("=" * 50)
