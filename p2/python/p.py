#!/usr/bin/py

import sys

def fib():
    a = 1
    b = 2
    total = 0
    max = int(sys.argv[1])
    while a < max:
        if (a%2 == 0):
            total += a
        tmp = a + b
        a = b
        b = tmp
    return total
print (fib())
