# coding: utf-8
'''
n! means n * (n - 1) * (n - 2) * .... * 3 * 2 * 1 
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

from timeit import default_timer as timer

def calculatefactorial(number):
    previous_factor = 0
    is_odd = False
    limit = number // 2
    x = 0
    result = 1

    if number & 1 != 0:
        is_odd = True
        number -= 1

    while x < limit:
        previous_factor = previous_factor + (number - 2 * x)
        result *= previous_factor
        x += 1

    if is_odd:
        result *= (number + 1)
    
    return result

if __name__ == '__main__':
    number = int(input('Enter the number :: '))
    start = timer()
    sum = 0
    fact = calculatefactorial(number)
    print('Factorial of {} is {}'.format(number, fact))
    while fact != 0:
        sum += fact % 10
        fact /= 10
    print('Sum of digits of factorial of {} is {}'.format(number, sum))
    end = timer()
    print('Time taken is {}'.format(end - start))

