'''
    Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

    d1 = 4*n^2 + 4*n + 1
    d2 = 4*n^2 + 2*n + 1
    d3 = 4*n^2 - 2*n + 1
    d4 = 4*n^2 + 1

    sum = d1 + d2 + d3 + d4 + 1
    sum = 16*n^2 + 4*n + 4 for n = 1,2,3...
    sum = 16 * (n * (n + 1) * (2*n + 1)) // 6 + (4 * (n * (n + 1)) // 2) + 4 * n
    sum = 8 * ((n * (n + 1) * (2*n + 1)) // 3) + 2 * (n * (n + 1)) + 4 * n
    n = (n - 1) // 2 # minus 1 because it does not start from 0
    temp = (8*n*n + 15*n + 13)
    sum = 1 + ((2 * n * temp) // 3)
'''

number = int(input('Enter the number :: '))
number = (number - 1) // 2
temp = (8*number*number + 15*number + 13)
sum = 1 + ((2 * number * temp) // 3)
print('Sum of diagonals is :: {}'.format(sum))