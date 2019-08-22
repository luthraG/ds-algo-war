# coding: utf-8
'''
    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!

Algorithm 2:: Use recursive approach
'''

from timeit import default_timer as timer

def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)

if __name__ == '__main__':
    number = int(input('Enter the number :: '))
    start = timer()
    fact = factorial(number)
    sum = 0
    while fact != 0:
        sum += fact % 10
        fact //= 10

    print('Sum of digits in factorial of {} is {}'.format(number, sum))
    end = timer()
    print('Time taken is : {}'.format(end - start))
