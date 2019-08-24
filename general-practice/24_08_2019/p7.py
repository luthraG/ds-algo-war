'''
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes not greater than given N.

    Input Format

    The first line contains an integer T i.e. number of the test cases. 
    The next T lines will contains an integer N.

    Constraints

    1 <= T <= 10^4
    1 <= N <= 10^6

    Output Format

    Print the value corresponding to each test case in separate line.

    Algorithm 4: Here we use sieve of rwh1
'''

from timeit import default_timer as timer

def sumOfPrimes(number):
    sum = 2
    number = number + 1
    primes = [True] * (number // 2)
    limit = int(number ** 0.5) + 1

    for i in range(3, limit, 2):
        if primes[i//2]:
            primes[i*i//2::i] = [False]*((number - i*i - 1)//(2*i) + 1)
    
    for i in range(1, number // 2):
        if primes[i]:
            sum += (2 * i + 1)

    return sum

if __name__ == '__main__':
    number = int(input('Enter then number :: '))
    start = timer()
    print('Sum of primes not greater than {} is {}'.format(number, sumOfPrimes(number)))
    end = timer()
    print('Time taken is : {}'.format(end - start))
