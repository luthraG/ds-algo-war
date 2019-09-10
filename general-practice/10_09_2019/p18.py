'''
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
'''

from timeit import default_timer as timer

def primes_rwh(upper_limit):
    upper_limit -= 1
    primes = [True] * upper_limit
    primes[0] = False
    primes[1] = False

    i = 3
    limit = int(upper_limit ** 0.5) + 1

    while i <= limit:
        if primes[i]:
            primes[i*i::2*i] = [False]*((upper_limit - i*i - 1)//(2*i) + 1)
        i += 2
    
    sum = 0

    if upper_limit == 2:
        sum = 2
    elif upper_limit > 2:
        i = 3
        sum = 2
        while i < upper_limit:
            if primes[i]:
                sum += i
            i += 2

    return sum

upper_limit = int(input('Enter the upper limit for finding sum of primes = '))
start = timer()
sum = primes_rwh(upper_limit)
end = timer()
print('Sum of primes below {} is {}'.format(upper_limit, sum))
print('Time taken is {}'.format(end - start))
