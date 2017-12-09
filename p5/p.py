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
    l=[]
    x = 2
    while n > 1:
        if n%x == 0:
            l.append(x)
            n = n/x
        else:
            x = nextprime(x)
    return l

def run():
    l=[]
    tmp=[]
    for x in range (1, 21):
       tmp=getprimefactor(x)
       for member in tmp:
           if (tmp.count(member) > l.count(member)):
               s = tmp.count(member) - l.count(member)
               for k in range (1, s+1):
                   l.append(member)
    total=1
    for x in l:
        total=total*x
    print (total)

run()






















