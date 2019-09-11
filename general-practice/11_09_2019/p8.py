'''
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
'''

from timeit import default_timer as timer

def rwh_primes(upper_limit):
    primes = [True] * upper_limit

    sum_of_primes = 0
    if upper_limit > 2:
        sum_of_primes += 2
    else:
        return sum_of_primes
    
    limit = int(upper_limit ** 0.5) + 1
    i = 3
    while i <= limit:
        if primes[i]:
            primes[i*i::2*i] = [False]*((upper_limit-i*i-1)//(2*i) + 1)
        i += 2
    
    i = 3
    while i < upper_limit:
        if primes[i]:
            sum_of_primes += i
        
        i += 2

    return sum_of_primes

upper_limit = int(input('Enter upper limit :: '))

start = timer()

sum_of_primes = rwh_primes(upper_limit)

end = timer()
print('Sum of primes below {} is {}'.format(upper_limit, sum_of_primes))