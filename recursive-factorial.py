#!/usr/bin/python3
import sys

print("Input number lemme run the factorial for you sharp sharp :)")

if len(sys.argv) <= 1:
    factNum = int(input())
else:    
    factNum = int(sys.argv[1])

def factorial(n):
    if (n <= 1):
        return 1;
    return n * factorial(n - 1)

def fac(n):
    if (n <= 1):
        return 1;
    return str(n) + " X " + str(fac(n - 1))



print(str(factNum) + " factorial (!" + str(factNum) + " or " + str(fac(factNum)) + ") = " + str(factorial(factNum)))

