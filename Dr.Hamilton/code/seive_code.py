from math import isqrt
import time

def prime(n):
    if n <= 2:
        return []
    primes = [True] * n
    primes[0]= False
    primes[1] = False
    primes[2] = True
    
    for a in range(2,isqrt(n)):
        if primes[a]:
            for x in range(a*a,n,a):
                primes[x] = False
    
    return [i for i in range(n) if primes[i]]

    
t0 = time.time()
# print(prime(10000000))
prime(100000000)
t1 = time.time()

print(t1-t0)