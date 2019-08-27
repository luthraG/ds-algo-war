'''
    The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

    How many circular primes are there below one million?

    length of a number = floor(1 + log N(in base 10))
    all rotations of a number:
        loop through 1 to number of digits
        p = pow(10, length of number) - 1
        and for each loop
            (n + (n mod 10 * p)) // 10
'''

from timeit import default_timer as timer
import math

def calculateExponent(base, exp):
    if base == 0 or base == 1 or exp == 1:
        return base
    elif exp == 0:
        return 1
    elif exp & 1 != 0:
        return base * calculateExponent(base * base, (exp - 1) // 2)
    else:
        return calculateExponent(base * base, exp // 2)

def precalculatePower():
    power = {}
    x = 1
    while x < 10:
        power[x] = calculateExponent(10, x)
        x += 1
    return power

def allRotationsPrime(sieve, powers, number):
    length = int(1 + math.log(number, 10))
    p = powers[length] - 1
    x = 1
    while x < length:
        number = (number + ((number % 10) * p)) // 10
        if sieve[number] == False:
            return False
        x += 1

    return True

def precalculateSieve(number):
    number += 1
    primes = [True] * number
    sieve = [False] * number
    i = 3

    primes[0] = False
    primes[1] = False

    limit = int(number ** 0.5) + 1
    while i < limit:
        if primes[i]:
            primes[i*i::2*i] = [False] * (((number - i * i - 1)// (2 * i)) + 1)
        i += 2
    
    i = 3
    sieve[2] = True
    while i < number:
        if primes[i]:
            sieve[i] = True
        i += 2
    
    return sieve

if __name__ == '__main__':
    number = int(input('Enter the upper limit of number : '))
    start = timer()
    sieve = precalculateSieve(number)
    power = precalculatePower()
    x = 2
    count = 0
    while x < number:
        if sieve[x] and allRotationsPrime(sieve, power, x):
            count += 1
        x += 1
    print('Number of circular primes below {} are {}'.format(number, count))
    end = timer()
    print('Time taken is : {}'.format(end - start))

