import random
import time

def keyGen():
    startTime = time.time()
    p = largePrime()
    print('I found p = ', p)
    q = largePrime()
    print('I found q = ', q)
    n = p*q
    print('Public key is: ', n)
    phin = lcm(p, q)
    print('I found phi(n): ', phin)
    e = genE(phin)
    print('The secret e is: ', eke)
    d = pow(e, -1, phin)
    print('I am d: ', d)
    endTime = time.time()
    totalTime = endTime - startTime
    print('The whole process took me: ', totalTime, 'seconds')
            
def gcd(a , b):
    if a == 0:
        return b
    return gcd(b % a, a) 

def relativelyPrime(a , b):
    return gcd(a,b) == 1

def genE(phin):
    e = random.getrandbits(28)
    while gcd(e, phin) != 1:
        e = random.getrandbits(28)
    return int(e)

def lcm(p, q):
    r = gcd(p, q)
    m = (abs(p*q)/r)
    return int(m)

def largePrime():
    n = random.getrandbits(28)
    while pow(2, n-1, n) != 1:
        n = random.getrandbits(28)
    return n

