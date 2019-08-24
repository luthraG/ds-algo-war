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

    Algorithm 1: Brute force, generates all the numbers below specified number and add those

        There is an optimization, all primes must either be of 6k + 1 or 6k - 1
        So we take a step of 6 for next number to check for prime
        and for prime number we check upto square root of number
'''

from timeit import default_timer as timer

def isPrime(number):
    if number <= 1:
        return False

    if number % 2 == 0:
        return number == 2
    if number % 3 == 0:
        return number == 3
    
    x = 5
    limit = int(number ** 0.5) + 1
    while x <= limit:
        if number % x == 0:
            return False
        if number % (x + 2) == 0:
            return False
        
        x += 6
    
    return True

if __name__ == '__main__':
    number = int(input('Enter the number : '))
    start = timer()
    sum = 0
    n = 0

    if number <= 2:
        sum += 2
    else:
        sum += 5
    if number >= 5:
        while n <= number:
            n += 6
            if isPrime(n - 1) and (n - 1) <= number:
                sum += (n - 1)
            
            if isPrime(n + 1) and (n + 1) <= number:
                sum += (n + 1)
        
    
    print('Sum of primes lesser than equal to {} is {}'.format(number, sum))
    end = timer()
    print('Time taken is : {}'.format(end - start))