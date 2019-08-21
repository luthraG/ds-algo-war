'''
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?
'''

from timeit import default_timer as timer

def calculatePower(base, power):
    if power == 0:
        return 1
    elif base == 0:
        return 0
    elif power == 1:
        return base
    elif base == 1:
        return 1
    elif power & 1 != 0:
        return base * calculatePower(base * base, (power - 1) // 2)
    else:
        return calculatePower(base * base, power // 2)

if __name__ == '__main__':
    base = int(input('Enter the base :: '))
    power = int(input('Enter power :: '))
    sum = 0
    start = timer()

    number = calculatePower(base, power)
    print('Resultant number : {}'.format(number))
    while number != 0:
        digit = number % 10
        sum = sum + digit
        number = number // 10
    print('Sum of digits of resultant number is {}'.format(sum))
    end = timer()
    print('Time taken is {}'.format(end - start))

