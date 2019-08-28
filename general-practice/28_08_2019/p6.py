from timeit import default_timer as timer
import math

def rwh_prime(upper_bound, number):
    primes = [True]  * upper_bound
    primes[0] = False
    primes[1] = False

    i = 3
    limit = int(upper_bound ** 0.5) + 1
    while i <= limit:
        if primes[i]:
            primes[i*i::2*i] = [False] * ((upper_bound-i*i- 1)//(2*i) + 1)
        i += 2

    i = 3
    count = 1
    nthPrime = -1
    if number == 1:
        nthPrime = 2

    while i < upper_bound and nthPrime == -1:
        if primes[i]:
            count += 1
        if count == number:
            nthPrime =  i
            break
        i += 2

    return nthPrime

if __name__ == '__main__':
    test_cases = int(input('Enter the number of test_cases :: '))
    for t in range(test_cases):
        number = int(input('Enter the number :: '))
        start = timer()
        firstPrimes = [2, 3, 5, 7, 11, 13]
        primes = -1
        if number < 7 and number > 0:
            prime = firstPrimes[number - 1]
        else:
            upper_bound = (number * math.log(number)) + (number * math.log(math.log(number))) + 3
            upper_bound = int(upper_bound)
            prime = rwh_prime(upper_bound, number)
        
        print('{} prime number is {}'.format(number, prime))
        end = timer()
        print('Time taken is : {}'.format(end - start))
