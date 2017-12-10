#!/usr/bin/py

import sys
def nextprime(n):
    n = n + 1
    while True:
        l = 0
        for x in range (2, n):
            l = x
            if (n%x == 0):
                break
        if (l == n-1):
            return n
        n = n + 1


def largestfactor():
    n = int(sys.argv[1])
    number = 1
    p = 2
    while number < n:
        if (n%p == 0):
            number = number * p
            bp = p
        p = nextprime(p)
        if (p > n):
            return bp
    return bp

print (largestfactor())
