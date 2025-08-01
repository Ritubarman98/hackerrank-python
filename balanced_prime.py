from math import sqrt
from itertools import count
def isprime(n):
    if n<2:
        return False
    sqr=int(sqrt(n))
    for i in range(2, sqr+1):
        if n%i==0:
            return False
    return True
def previous_prime(n):
    for i in range(n-1, 1,-1):
        if isprime(i):
            return i
def next_prime(n):
    for i in count(n+1):
        if isprime(i):
            return i
def isbalanceprime(n):
    if isprime(n):
        prev=previous_prime(n)
        nextprime=next_prime(n)
        if (prev+nextprime)//2 == n:
            return True
        return False
    return False
n=int(input())
if 1<=n<=10000:
    if isbalanceprime(n):
        print(n, "is Balanced Prime")
    else:
        print(n, "is not Balanced Prime") 
        