# coding: utf-8
'''
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

    This is the problem of finding LCM of all numbers which can be found by repeatedly finding LCM of two numbers
    and LCM of two numbers can be found by multiplying two numbers and dividing it by GCD
'''

from timeit import default_timer as timer

def gcd(a, b):
    if a == 0 or b == 0:
        return 0

    if a > b:
        num = a
        den = b
    else:
        num = b
        den = a

    rem = num % den

    while rem != 0:
        num = den
        den = rem
        rem = num % den

    return den

def lcm(a, b):
    return (a // gcd(a, b)) * b

if __name__ == '__main__':
    number = int(input('Enter upper limit of number :: '))
    start = timer()
    x = 1
    leastMultiple = 1
    while x <= number:
        leastMultiple = lcm(x, leastMultiple)
        x += 1

    print('LCM of all number from 1 to {} is {}'.format(number, leastMultiple))
    end = timer()
    print('Time taken is : {}'.format(end - start))
