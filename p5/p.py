def nextprime(i):
    i = i + 1
    while True:
        for x in range (2, i):
            if (i%x == 0):
                break
        if (x == i-1):
           # print (i)
            return i
        #print (i)
        i = i + 1

def getprimefactor(n):
    for x in range (1, n):
        k = nextprime(x)



nextprime(2)





















