# coding: utf-8
'''
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?
'''

from timeit import default_timer as timer

def calculateExp(base, power):
    if power == 0:
        return 1
    elif power == 1:
        return base
    elif base == 0:
        return 0
    elif base == 1:
        return 1
    elif power & 1 != 0:
        return base * calculateExp(base * base, (power - 1) // 2)
    else:
        return calculateExp(base * base, power // 2)

if __name__ == '__main__':
    number = int(input('Enter the power :: '))
    base = 2
    start = timer()
    sum = 0
    exp = calculateExp(base, number)
    while exp != 0:
        sum += exp % 10
        exp = exp // 10
    print('Sum of digits in {} raised to {} is {}'.format(base, number, sum))
    end = timer()
    print('Time taken is : {}'.format(end - start))
