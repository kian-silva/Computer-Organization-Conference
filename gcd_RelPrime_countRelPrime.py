
def gcd(a , b):
    if a > b:
        small = b
    else:
        small = a
    for i in range(1, small+1):
        if ((a % i == 0) and (b % i == 0)):
            gcd = i

    return gcd 

def relativelyPrime(a , b):
    return gcd(a,b) == 1

def primes(n):
    if n < 1:
        return False
    for i in range(2, n):
        if n % i == 0:
             return False
    return True

def countRelPrimes(n):
    count = 0
    for i in range(1, n):
        if primes(i):
            if relativelyPrime(i, n):
                 count += 1
        else:
            if relativelyPrime(i, n):
                count += 1
    return count
    
    
