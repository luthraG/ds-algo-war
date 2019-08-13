from timeit import default_timer as timer

if __name__ == '__main__':
    start = timer()

    limit = 10000
    addition = 0
    for x in range(1, limit):
        if x % 3 == 0 or x % 5 == 0:
            addition = addition + x
    end = timer()
    print("Sum of multiples of 3 and 5 below {} is {}".format(limit, addition))
    print("Time taken {}".format(end - start))
