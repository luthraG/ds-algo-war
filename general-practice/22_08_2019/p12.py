# coding: utf-8
'''
    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!

Algorithm 3:: Use pattern of first and last term to reduce number of multiplications
'''

from timeit import default_timer as timer

def calculateFactorial(number):
    previous_factor = 0
    fact = 1
    is_odd = False
    if number & 1 == 1:
        is_odd = True
        number -= 1

    limit = number // 2
    x = 0
    while x < limit:
        previous_factor = previous_factor + (number - 2 * x)
        fact *= previous_factor
        x += 1

    if is_odd:
        fact *= (number + 1)
    return fact

if __name__ == '__main__':
    number = int(input('Enter the number :: '))
    start = timer()
    sum = 0
    fact = calculateFactorial(number)
    while fact != 0:
        sum += fact % 10
        fact //= 10

    print('Sum of digits in factorial of {} is {}'.format(number, sum))
    end = timer()
    print('Time taken is : {}'.format(end - start))
