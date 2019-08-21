'''
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
'''

from timeit import default_timer as timer
import math

def isPrime(num):
    if num % 2 == 0 and num != 2:
        return False
    
    limit = int(math.sqrt(num)) + 1
    for x in range(3, limit, 2):
        if num % x == 0:
            return False
    return True

if __name__ == '__main__':
    number = int(input('Enter the number :: '))
    start = timer()
    sum = 0
    i = 2
    while i < number:
        if isPrime(i):
            sum += i
        i += 1
    
    print('Sum of primes below {} is {}'.format(number, sum))
    end = timer()
    print('Time taken is : {}'.format(end - start))