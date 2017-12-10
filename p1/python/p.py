#!/usr/bin/python
import sys
def allmultiples():
    below = int (sys.argv[1])
    x = 3
    y = 5
    sum=0
    count = 0
    while count < below:
        if (count%x == 0):
            sum+=count
        elif (count%y == 0):
            sum+=count
        count+=1
    return sum
print (allmultiples())




























