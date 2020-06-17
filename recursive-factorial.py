#!/usr/bin/python3

print("Input number lemme run the factorial for you sharp sharp :)")

factNum = int(input())

def factorial(n):
    if (n <= 1):
        return 1;
    return n * factorial(n - 1)

def fac(n):
    if (n <= 1):
        return 1;
    return str(n) + " X " + str(fac(n - 1))



print(str(factNum) + " factorial (!" + str(factNum) + " or " + str(fac(factNum)) + ") = " + str(factorial(factNum)))

