# coding: utf-8
'''
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
'''

from timeit import default_timer as timer
import math

def isPrime(number):
    if number % 2 == 0:
        return number == 2
    elif number % 3 == 0:
        return number == 3
    else:
        x = 5
        limit = int(math.sqrt(number) + 1)
        while x <= limit:
            if number % x == 0:
                return False
            if number % (x + 2) == 0:
                return False
            x += 6
        return True

if __name__ == '__main__':
    number = int(input('Enter the upper limit :: '))
    start = timer()
    x = 2
    sum = 0

    while x < number:
        if isPrime(x):
            sum += x
        x += 1
    print('Sum of primes below {} is {}'.format(number, sum))
    end = timer()
    print('Time taken is : {}'.format(end - start))
