import numpy as np

def isprime(n):
    prime = True
    for i in range(2, int(n**0.5)+1):               #Only need to check to sqrt(n)
        if n%i == 0:
            prime = False
    if prime:
        print('The number', n, 'is prime.')
        return True
    else:
        print('The number', n, 'is not prime.')
        return False

def nprimes(N):
    primes = np.array([2])                          #Only need to compare divisibility by a prime number. Record the list of primes
    n = 3

    while len(primes) != N:
        if any((n%primes[primes <= n**0.5] == 0)):  #Check divisibility with each prime factor up to sqrt(n)
            n += 1
        else:
            primes = np.append(primes, [n])         #If it is a new prime number, add it to the list
            n += 1
    return primes

def a2bprimes(a, b):
    primes = np.array([], dtype = int)              #Pretty much the same thing as before
    for n in range(a, b+1):
        prime = True
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                prime = False
        if prime:
            primes = np.append(primes, [n])
    return primes

def primefac(n):
    print(n, '= ', end = '')
    for k in range(2, int((n+1)/2)):                #Only need to compare up to n/2 since 2 is the smallest prime (wont give factorisation for a prime)
        while n%k == 0:
            n = n/k
            print(k, end = '')
            if n > k:
                print('*', end = '')

