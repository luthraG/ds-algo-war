'''
The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

from timeit import default_timer as timer

if __name__ == '__main__':
    number = int(input('Enter the number :: '))
    start = timer()
    sum1 = number * (number + 1) // 2
    sum2 = sum1 * (2*number + 1) // 3
    diff = (sum1 * sum1) - sum2
    print('Different of sum of squares from square of sum = {}'.format(diff))
    end = timer()
    print('Time taken is : {}'.format(end - start))
