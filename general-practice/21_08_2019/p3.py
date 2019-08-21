'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from timeit import default_timer as timer
import math

def primeFactors(number):
    factors = []
    while number % 2 == 0:
        factors.append(2)
        number //= 2
    
    # Now number must be odd
    x = 3
    limit = int(math.sqrt(number)) + 1
    while x < limit:
        while number % x == 0:
            factors.append(x)
            number //= x
        x += 2 # Since next odd number will have a difference of 2
    
    # If number if greater than 2 then we need to use number as factor as well
    if number > 2:
        factors.append(number)

    return factors

if __name__ == '__main__':
    number = int(input('Enter the number :: '))
    start = timer()
    factors = []
    factors = primeFactors(number)
    if len(factors):
        print('Greatest prime factor of {} is {}'.format(number, factors[len(factors) - 1]))
    end = timer()
    print('Time taken is {}'.format(end - start))