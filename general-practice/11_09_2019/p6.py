'''
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10001st prime number?
'''

from timeit import default_timer as timer
import math

def prime_rwh(upper_limit, number):
    primes = [True]* upper_limit
    primes[0] = False
    primes[1] = False

    i = 3
    limit = int(upper_limit ** 0.5) + 1
    while i <= limit:
        primes[i*i::2*i] = [False]*((upper_limit-i*i-1)//(2*i) + 1)
        i += 2

    count = 1
    i = 3
    nthPrimeNumber = -1
    
    while i < upper_limit:
        if primes[i]:
            count += 1
        if count == number:
            nthPrimeNumber = i
            break
        i += 2
    
    return nthPrimeNumber

number = int(input('Enter which prime number is required :: '))
start = timer()

primes = [2,3,5,7,11,13]
if number < 7:
    nthPrimeNumber = primes[number - 1]
else:
    upper_limit = int((number * math.log(number)) + (number * math.log(math.log(number))) + 3)
    nthPrimeNumber = prime_rwh(upper_limit, number)

end = timer()
print('{} prime number is {}'.format(number, nthPrimeNumber))
print('Time taken is {}'.format(end - start))