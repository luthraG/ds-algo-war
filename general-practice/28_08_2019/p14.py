from timeit import default_timer as timer
import math

def calculateExponent(base, exp):
    if base == 0 or base == 1 or exp == 1:
        return base
    elif exp == 0:
        return 1
    elif exp & 1 == 1:
        return base * calculateExponent(base * base, (exp - 1) // 2)
    else:
        return calculateExponent(base * base, exp // 2)

def precalculatePowers(n):
    x = 1
    powers = [0] * 10
    while x < 10:
        powers[x] = calculateExponent(x, n)
        x += 1
    
    return powers

def calculateUpperBound(powers, exp):
    log9 = 1 + (exp * math.log(9, 10))
    x = 1
    while x < 1000:
        temp = math.log(x, 10) + log9
        if x <= temp and temp < (x + 1):
            return x * powers[9]
        x += 1
    
    return 0

def sumOfPowers(powers, number):
    sum = 0
    while number != 0:
        sum += powers[number % 10]
        number //= 10
    
    return sum

if __name__ == '__main__':
    power = int(input('Enter the power :: '))
    start = timer()
    powers = precalculatePowers(power)
    upper = calculateUpperBound(powers, power)
    x = 10
    sum = 0
    while x <= upper:
        num = sumOfPowers(powers, x)
        if num == x:
            sum += num
        x += 1
    end = timer()
    print('Sum of all number that be expressed as sum of powers of digits = {}'.format(sum))
    print('Time taken is {}'.format(end - start))