'''
rwh prime
'''

from timeit import default_timer as timer
import math

def rwh_primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [2*i + 1 for i in range(1,n//2) if sieve[i]]

def rwh_primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

if __name__ == '__main__':
    number = int(input('Enter the number :: '))
    start = timer()
    n = int(number * (math.log(number) + math.log(math.log(number)))) + 3
    primes = rwh_primes1(n)
    # print(primes)
    print(primes[number - 1])
    end = timer()
    print('Time taken : {}'.format(end - start))
