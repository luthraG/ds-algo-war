from timeit import default_timer as timer
import math


def getPrimeFactors(number):
    factors = []

    if number > 1:
        while number % 2 == 0:
            factors.appned(2)
            number = number // 2

        for x in range(3, int(math.sqrt(number)) + 1, 2):
            while number % x == 0:
                factors.append(x)
                number = number // x

        if number > 2:
            factors.append(number)
    return factors

if __name__ == '__main__':
    start = timer()
    number = 600851475143
    factors = getPrimeFactors(number)
    end = timer()
    print("Prime factors of {} are {}".format(number, factors))
    print("Largest prime factor of {} is {}".format(number, factors[len(factors) - 1]))
    print("Time taken is {}".format(end - start))
