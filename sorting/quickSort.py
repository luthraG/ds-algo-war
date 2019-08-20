from timeit import default_timer as timer

def partition(input, low, high):
    # print("low {} and high {}".format(low, high))
    i = low - 1 # Index of smaller element

    pivot = input[high]
    j = low # loop variable
    while j < high:
        elem = input[j]
        if elem <= pivot:
            # Increment the counter and then replace i with j
            i += 1
            temp = input[j]
            input[j] = input[i]
            input[i] = temp
        j += 1
    i += 1
    temp = input[i]
    input[i] = pivot
    input[high] = temp
    
    return i

def quickSort(input, low, high):
    if low < high:
        partitionIndex = partition(input, low, high)

        # Now pivot is at correct position, so we will sort left and sort right
        quickSort(input, low, partitionIndex - 1)
        quickSort(input, partitionIndex + 1, high)

if __name__ == "__main__":
    input = [4, 1, 3, 7, 9, 8, 2, 6, 5]
    # input = [10, 7, 8, 9, 1, 5] 
    start = timer()
    quickSort(input, 0, len(input) - 1)
    print("Sorted list is {}".format(input))
    end = timer()
    print("Time taken is {}".format((end - start)))