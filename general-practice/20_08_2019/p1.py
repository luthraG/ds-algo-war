# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 10 Million.

from timeit import default_timer as timer

if __name__ == '__main__':
    start = timer()
    number = 1000

    # Since we want below hence
    number -= 1

    # Sum of multiple of 3s
    upper3 = number // 3
    sum3 = 3 * upper3 * (upper3 + 1) // 2

    # Sum of multiple of 5s
    upper5 = number // 5
    sum5 = 5* upper5 * (upper5 + 1) // 2

    # Sum of multiple of 15s
    upper15 = number // 15
    sum15 = 15 * upper15 * (upper15 + 1) // 2

    sum = sum3 + sum5 - sum15
    print("sum3 {}, sum5 {} and sum15 {}".format(sum3, sum5, sum15))
    print("Overall sum = {}".format(sum))

    end = timer()
    print("Time taken is {}".format(end - start))