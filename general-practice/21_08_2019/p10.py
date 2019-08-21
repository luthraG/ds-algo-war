# coding: utf-8
'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

from timeit import default_timer as timer

def CalculateFactorial(number):
    primes = [True]*(number + 1)
    result = 1
    primes[0] = False
    primes[1] = False
    i = 2
    while i <= number:
        if primes[i]:
            j = i + i
            while j <= number:
                primes[j] = False
                j += i
            sum = 0
            t = i
            while t <= number:
                sum += (number // t)
                t *= i
            result *= i**sum
        i += 1
    return result

if __name__ == '__main__':
    number = int(input('Enter number :: '))
    start = timer()
    sum = 0
    fact = CalculateFactorial(number)
    print("Factorial of {} is {}".format(number, fact))
    while fact !=  0:
        sum += fact % 10
        fact //= 10
    print('Sum of digits of factorial of {} is {}'.format(number, sum))
    end = timer()
    print('Time taken is {}'.format(end - start))
