'''
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to N?
'''

def GCD(a, b):
    if a > b:
        num = a
        den = b
    else:
        num = b
        den = a

    rem = num % den

    while rem != 0:
        num = den
        den = rem
        rem = num % den
    
    return den

def LCM(a, b):
    return ((a // GCD(a, b)) * b)

upper_limit = int(input('Enter upper limit of the range from 1 to N for finding the number they evenly divides :: '))
i = 1
prod = 1
while i < upper_limit:
    prod = LCM(prod, i)
    i += 1

print('Smallest number that is evenly divided by all numbers from 1 to {} is {}'.format(upper_limit, prod))