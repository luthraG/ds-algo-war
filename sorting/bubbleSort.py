from timeit import default_timer as timer

def sortNumbers(input):
    i = 0
    iterations = 0
    length = len(input)
    while i < length - 1:
        j = 0
        while j < length - 1 - i:
            iterations += 1
            item1 = input[j]
            item2 = input[j +  1]
            if item1 > item2:
                input[j + 1] = item1
                input[j] = item2
            j += 1
        i += 1

    print("Iterations taken {}".format(iterations))
    return input

if __name__ == '__main__':
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 14]
    start = timer()
    print("Sorted numbers : {}".format(sortNumbers(input)))
    end = timer()
    print("Time taken is {}".format(end - start))