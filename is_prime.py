import time
from functools import lru_cache
## there are four optimized prime finding algorithms here. when n=10000000 runtime in seconds
##V2:  214.51220083236694
##V3:  112.14515471458435
##V4:  45.26100540161133
def is_prime_v1(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
    return True

def is_prime_v2(n):
    if n>1:
        for i in range(2,(int(n**(0.5))+1)):
            if n%i==0:
                return False
    else:
        return False
    return True

def is_prime_v3(n):
    if n==2:
        return True
    elif n>2 and n%2!=0:
        for i in range(3,(int(n**(0.5))+1),2):
            if n%i==0:
                return False
    else:
        return False
    return True

lru=[2]
def is_prime_v4(n):
    global lru
    if n==2:
        return True
    elif n>2 and n%2!=0:
        x=int(n**(0.5))+1
        for i in lru:
            if i>x:
                break
            elif n%i==0:
                return False
    else:
        return False
    lru+=[n]
    return True    

#print(is_prime_v4())
##for i in range(2,10000):
##    if is_prime_v4(i):
##        print(i," ", end = '')
##    if is_prime_v3(i):
##        print(i)
n=10000000
to=time.time()
for i in range(n):
    is_prime_v2(i)
print("V2: ",time.time()-to)

to=time.time()
for i in range(n):
    is_prime_v3(i)
print("V3: ",time.time()-to)

to=time.time()
for i in range(n):
    is_prime_v4(i)
print("V4: ",time.time()-to)
