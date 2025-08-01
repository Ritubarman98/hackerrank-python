from math import sqrt
def isprime(n):
    if n<2:
        return False
    sqr=int(sqrt(n))
    for i in range(2, sqr+1):
        if n%i==0:
            return False
    return True
def issemiprime(n):
    count=0
    for i in range(1,n):
        if n%i==0 and isprime(i):            
            x=n//i
            if isprime(x):
                count +=1
    if count >0:
        return True
    return False
def ischenprime(n):
    if isprime(n):
        if isprime(n-2) or issemiprime(n-2):
            return True
        return False
    return False
        
n=int(input())
if 1<=n<=10000:
    if ischenprime(n):
        print("Yes")
    else:
        print("No")
