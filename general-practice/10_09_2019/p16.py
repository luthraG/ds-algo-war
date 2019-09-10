'''
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10,001st prime number?

    Upper limit when n > 6
    N * (log N) + N * (log(log N))
'''

import math

def sieve_rwh(upper_limit, number):
    primes = [True] * upper_limit
    primes[0] = False
    primes[1] = False

    i = 3
    limit = int(upper_limit ** 0.5) + 1
    while i <= limit:
        if primes[i]:
            primes[i*i::2*i] = [False] * ((upper_limit - i*i - 1)//(2*i) + 1)
        i += 2
    
    nthPrime = -1
    count = 1
    i = 3

    if number == 1:
        nthPrime = 2
    else:
        while i < upper_limit:
            if primes[i]:
                count += 1
            if count == number:
                nthPrime = i
                break
            i += 2
    return nthPrime

number = int(input('Enter the Nth value for which prime number required :: '))
if number < 7:
    primes = [2, 3, 5, 7, 11, 13]
    nthPrime = primes[number - 1]
else:
    upper_limit = (number * math.log(number)) + (number * math.log(math.log(number))) + 3
    upper_limit = int(upper_limit)
    nthPrime = sieve_rwh(upper_limit, number)

print('{} prime number is {}'.format(number, nthPrime))