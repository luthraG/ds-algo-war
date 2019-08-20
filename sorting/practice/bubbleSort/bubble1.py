from timeit import default_timer as timer

def bubbleSort(input):
    i = 0
    length = len(input)
    while i < length:
        j = 0
        while j < length - 1 - i:
            if input[j] > input[j + 1]:
                temp = input[j + 1]
                input[j + 1] = input[j]
                input[j] = temp
            j += 1
        i += 1

if __name__ == '__main__':
    input = [4, 1, 3, 7, 9, 8, 2, 6, 5]
    start = timer()
    bubbleSort(input)
    print("Sorted list is {}".format(input))
    end = timer()
    print("Time taken is : {}".format(end - start))
