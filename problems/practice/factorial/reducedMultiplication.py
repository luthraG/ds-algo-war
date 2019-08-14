from timeit import default_timer as timer

if __name__ == '__main__':
    number = int(input('Enter the number :: '))
    start = timer()
    previous_factor = 0
    is_odd = False
    fact = 1

    if number & 1 != 0:
        is_odd = True
        number = number - 1

    i = 0
    limit = number // 2

    while limit > 0:
        previous_factor = previous_factor + (number - (2 * i))
        fact = fact * previous_factor
        i = i + 1
        limit = limit - 1

    if is_odd:
        fact = fact * (number + 1)

    end = timer()
    print("Factorial of {} is {}".format(number, fact))
    print("Time taken is {}".format(end - start))
