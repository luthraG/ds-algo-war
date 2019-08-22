# coding: utf-8
'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

from timeit import default_timer as timer

if __name__ == '__main__':
    number = int(input('Enter the upper limit of number :: '))
    start = timer()
    diff = 0
    sum_n_terms = number * (number + 1) // 2
    diff = (sum_n_terms * sum_n_terms) - (sum_n_terms * (2 * number + 1) // 3)
    print('Difference between square of sum and sum of squares of 1 to {} numbers is {}'.format(number, diff))
    end = timer()
    print('Time taken is : {}'.format(end - start))
