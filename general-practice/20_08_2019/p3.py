'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

from timeit import default_timer as timer
import math

def primefactors(number):
    factors = []
    while number % 2 == 0:
        factors.append(2)
        number = number // 2
    
    # Now number must be odd
    i = 3
    upper = int(math.sqrt(number)) + 1
    while i < upper:
        while number % i == 0:
            factors.append(i)
            number = number // i
        i += 2 # Since next odd number is at plus 2

    # If number is greater than 2 then number must be prime
    if number > 2:
        factors.append(number)
    return factors

if __name__ == '__main__':
    start = timer()
    number = 600851475143
    factors = primefactors(number)
    print("Factors of {} are {}".format(number, factors))
    if len(factors):
        print("Largest prime factor is : {}".format(factors[len(factors) - 1]))
    end = timer()
    print("Time taken is : {}".format(end - start))