from timeit import default_timer as timer
import math


def isPrime(number):
    prime = True
    if number < 2:
        prime = False

    x = 2
    limit = int(math.sqrt(number)) + 1
    while x < limit:
        if number % x == 0:
            prime = False
            break
        x += 1

    return prime

if __name__ == '__main__':
    number = int(input('Enter the number :: '))
    start = timer()
    primes = []
    x = 1
    while x <= number:
        if isPrime(x):
            primes.append(x)
        x += 1
    end = timer()
    print("Primes lesser than {} are {}".format(number, primes))
    print('Time taken is : {}'.format(end - start))
