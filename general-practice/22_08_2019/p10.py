# coding: utf-8
'''
    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!

Algorithm 1:: Use simple  multiplication
'''

from timeit import default_timer as timer

if __name__ == '__main__':
    number = int(input('Enter the number :: '))
    number2 = number
    start = timer()
    fact = 1
    sum = 0
    while number > 0:
        fact *= number
        number -= 1
    
    while fact != 0:
        sum += fact % 10
        fact //= 10
    
    print('Sum of digits in factorial of {} is {}'.format(number2, sum))
    end = timer()
    print('Time taken is : {}'.format(end - start))
