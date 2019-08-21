'''
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

from timeit import default_timer as timer

def gcd(a, b):
    if a > b:
        num = a
        dev = b
    else:
        num = b
        dev = a
    rem = num % dev

    while rem != 0:
        num = dev
        dev = rem
        rem = num % dev

    return dev

def lcm(a, b):
    return (a // gcd(a, b)) * b

if __name__ == '__main__':
    number = int(input('Enter upper limit :: '))
    start = timer()
    leastMultiple = 1
    i = 1
    while i <= number:
        leastMultiple = lcm(i, leastMultiple)
        i += 1
    print('LCM of first {} numbers is {}'.format(number, leastMultiple))
    end = timer()
    print('Time taken is : {}'.format(end - start))