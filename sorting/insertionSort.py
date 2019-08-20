from timeit import default_timer as timer

def insertionSort(input):
    i = 1
    iterations = 0
    length = len(input)
    while i < length:
        item = input[i]
        j = i - 1
        while j >= 0 and item < input[j]:
            iterations += 1
            input[j + 1] = input[j]
            j -= 1
        input[j +  1] = item
        i += 1

    print("Total iterations taken = {}".format(iterations))
    return input

if __name__ == '__main__':
    input = [4, 1, 3, 7, 9, 8, 2, 6, 5]
    start = timer()
    print("Sorted list is : {}".format(insertionSort(input)))
    end = timer()
    print("Time taken is {}".format((end - start)))