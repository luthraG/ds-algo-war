# coding: utf-8
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Here we use sieve approach
'''

from timeit import default_timer as timer
import math

def sumOfPrimes(number):
    primes = [True] * number
    primes[0] = False
    primes[1] = False
    sum = 0
    i = 2
    while i < number:
        if primes[i]:
            sum += i
            j = i + i
            while j < number:
                primes[j] = False
                j += i
        i += 1
    return sum

if __name__ == '__main__':
    number = int(input('Enter the upper limit of number :: '))
    start = timer()
    print('Sum of all primes below {} is {}'.format(number, sumOfPrimes(number)))
    end = timer()
    print('Time taken is : {}'.format(end - start))
