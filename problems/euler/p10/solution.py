from timeit import default_timer as timer
import math


def isPrime(number):
    if number % 2 == 0 and number != 2:
        return False

    for x in range(3, int(math.sqrt(number)) + 1, 2):
        if number % x == 0:
            return False

    return True

if __name__ == '__main__':
    start = timer()
    number = 2000000
    addition = 0
    for x in range(2, number + 1):
        isP = isPrime(x)
        if isP:
            addition = addition + x
    print("Sum of prime numbers below {} is {}".format(number, addition))
    end = timer()
    print("Time taken is {}".format(end - start))
