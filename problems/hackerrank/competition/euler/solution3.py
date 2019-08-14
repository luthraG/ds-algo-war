from timeit import default_timer as timer
import math

if __name__ == '__main__':
    number = int(input("Enter the number :: "))
    start = timer()
    factors = []

    # Let us take out all 2s
    while number % 2 == 0:
        factors.append(2)
        number = number // 2

    # Let us take out odd number
    for x in range(3, int(math.sqrt(number)) + 1, 2):
        if number % x == 0:
            factors.append(x)
            number = number // x

    # Last check if number is greater than 2, if yes
    if number > 2:
        factors.append(number)
    end = timer()
    print("Prime factors of {} are {}".format(number, factors))
    if len(factors) > 0:
        print("Largest prime factor for {} is {}".format(number, factors[len(factors) - 1]))
    print("Time taken is {}".format(end - start))
