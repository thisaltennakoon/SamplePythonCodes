import  time
lru={}
def fib(n):    
    if n in lru:
        return lru[n]
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        a=fib(n-2)+fib(n-1)
        lru[n]=a
        return a


def Fib(n):
    a=0
    b=1
    c=1
    for i in range(n-1):
        c=a+b
        a=b
        b=c
    return c
t0=time.time()

from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibb(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibb(n-2)+fibb(n-1)


n=1000
t0=time.time()
x=Fib(n)
t1=time.time()
print (t1,t0)
