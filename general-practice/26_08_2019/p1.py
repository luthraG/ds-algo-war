'''
    Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4
    As 1 = 14 is not a sum it is not included.

    The sum of these numbers is 1634 + 8208 + 9474 = 19316.

    Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
from timeit import default_timer as timer
import math

def calculateExponent(base, exp):
    if base == 0 or base == 1 or exp == 1:
        return base
    elif exp == 0:
        return 1
    elif exp & 1 != 0:
        return base * calculateExponent(base * base, (exp - 1) // 2)
    else:
        return calculateExponent(base * base, exp // 2)

def precalculatePowers(n):
    powers = {}
    x = 0
    while x < 10:
        powers[x] = calculateExponent(x, n)
        x += 1
    return powers

def upperBound(powers, n):
    # 10 ^ (d - 1) <= d * 9 ^ n < 10 ^ d
    # d - 1 <= log d + n log 9 < d
    # d <= log d + (1 + n log 9) < d + 1
    upper = 0
    log9 = 1 + n * math.log(9, 10)
    x = 1
    while x < 1000:
        temp = math.log(x, 10) + log9
        if x <= temp and temp < x + 1:
            upper = x * powers[9]
            break
        x += 1

    return upper

def sumOfPowers(powers, number):
    sum = 0
    while number != 0:
        sum += powers[number % 10]
        number //= 10
    return sum

if __name__ == '__main__':
    power = int(input('Enter the power : '))
    powers = precalculatePowers(power)
    start = timer()
    upperBound = upperBound(powers, power)
    x = 10
    overallSum = 0
    while x <= upperBound:
        sum = sumOfPowers(powers, x)
        if x == sum:
            overallSum += sum
        x += 1
    print('Sum of numbers that can be written as sum of {} powers of digits is {}'.format(power, overallSum))
    end = timer()
    print('Time taken is : {}'.format(end - start))
