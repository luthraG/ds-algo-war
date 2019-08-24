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

    Algorithm 2: Here we use sieve of Eratosthenes
'''

from timeit import default_timer as timer

def sumOfPrimes(number):
    sum = 0
    primes = [True] * (number + 1)
    x = 2

    while x <= number:
        y = x
        if primes[y]:
            sum += x
            y = 2 * x
            while y <= number:
                primes[y] = False
                y += x
        x += 1

    return sum

if __name__ == '__main__':
    number = int(input('Enter the number : '))
    start = timer()
    print('Sum of primes not greater than {} is {}'.format(number, sumOfPrimes(number)))
    end = timer()
    print('Time taken is : {}'.format(end - start))
