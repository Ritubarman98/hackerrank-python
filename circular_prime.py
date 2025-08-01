from math import sqrt
def isprime(n):
    if n<2:
        return False
    sqr=int(sqrt(n))
    for i in range(2, sqr+1):
        if n%i==0:
            return False
    return True
def iscircularprime(n):
    s1=str(n)
    for i in range(len(s1)):
        s1=s1[-1]+s1[:-1]
        if not isprime(int(s1)):
            return False
    return True
n=int(input())
if 1<=n<=1000000:
    if iscircularprime(n):
        print("Yes")
    else:
        print("No")