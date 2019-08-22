# coding: utf-8
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from timeit import default_timer as timer

def findFactors(number):
    factors = []
    while number % 2 == 0:
        factors.append(2)
        number = number // 2
    
    x = 3
    while x <= number:
        while number % x == 0:
            factors.append(x)
            number = number // x
        x += 2
    # At this point if number is greater than 2 then number is prime
    if number > 2:
        factors.append(number)

    return factors

if __name__ == '__main__':
    number = int(input('Enter the number :: '))
    start = timer()
    factors = findFactors(number)
    if len(factors):
        print('Largest prime factor of {} is {}'.format(number, factors[-1]))
    end = timer()
    print('Time taken is : {}'.format(end - start))
