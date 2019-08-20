from timeit import default_timer as timer

def insertionSort(input):
    i = 1

    while i < len(input):
        item = input[i]
        j = i - 1
        while j >= 0 and input[j] > item:
            input[j + 1] = input[j]
            j -= 1
        input[j + 1] = item
        i += 1

if __name__ == '__main__':
    input = [4, 1, 3, 7, 9, 8, 2, 6, 5]
    start = timer()
    insertionSort(input)
    print("Sorted lits is {}".format(input))
    end = timer()
    print("Time taken is {}".format(end - start))
