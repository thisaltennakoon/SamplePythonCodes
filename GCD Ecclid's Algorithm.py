def gcd(A,B):
    a=max(A,B)
    b=min(A,B)
    r=a%b
    if r==0:
        return b
    else:
        a=b
        b=r
        return gcd(a,b)

def gcd_V2(A,B):
    a=max(A,B)
    b=min(A,B)
    r=a%b
    while r!=0:
        a=b
        b=r
        r=a%b
    return b
print(gcd_V2(8,20))
