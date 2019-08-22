# coding: utf-8
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

Algorithm is based on idea that prime numbers are always of the form 6*k + 1
So we would only check those numbers which can be expressed in 6*k + 1 form
'''

from timeit import default_timer as timer
import math

def isPrime(number):
    if number % 2 == 0:
        return number == 2
    
    if number % 3 == 0:
        return number == 3
    
    x = 5
    limit = int(math.sqrt(number) + 1)
    while x <= limit:
        if number % x == 0:
            return False
        if number % (x + 2) == 0:
            return False
        
        x += 6
    
    return True


def nthPrime(number):
    n = 0 # Keeps the nth prime number
    c = 2 # Keeps the counter of prime number

    if number == 1:
        n = 2
    elif number == 2:
        n = 3

    while c < number:
        n += 6

        if isPrime(n - 1):
            c += 1
            if c == number:
                return n - 1
        
        if isPrime(n + 1):
            c += 1
            if c == number:
                return n + 1

    return n

if __name__ == '__main__':
    number = int(input('Enter the number :: '))
    start = timer()
    print('{} prime number is {}'.format(number, nthPrime(number)))
    end = timer()
    print('Time taken is {}'.format(end - start))
