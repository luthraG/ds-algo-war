'''
    The sum of the squares of the first ten natural numbers is,

    1**2 + 2**2 + ... + 10**2 = 385
    The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)**2 = 552 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

upper_limit = int(input('Enter upper limit of number :: '))
sum_of_numbers = (upper_limit * (upper_limit + 1)) // 2
sum_of_squares = (sum_of_numbers * (2*upper_limit + 1)) // 3

diff = sum_of_numbers * sum_of_numbers - sum_of_squares
print('Difference between these numbers are {}'.format(diff))