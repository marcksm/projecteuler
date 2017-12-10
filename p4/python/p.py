#!/usr/bin/python

def ispalindrome(n):
    if (str(n) == str(n)[::-1]):
        return True
    return False

def check():
    max = 0
    for x in range (100, 1000):
        for y in range (100, 1000):
            if (ispalindrome(x*y)):
                if (x*y > max):
                    max = x*y
    return max

print (check())



















