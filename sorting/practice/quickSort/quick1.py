from timeit import default_timer as timer

def partition(input, low, high):
    i = low - 1
    pivot = input[high]
    j = low
    while j < high:
        elem = input[j]
        if elem <= pivot:
            i += 1
            input[j], input[i] = input[i], input[j]
        j += 1
    i += 1
    input[i], input[high] = pivot, input[i]
    return i

def quickSort(input, low, high):
    if low < high:
        partitionIndex = partition(input, low, high)

        # Pivot is at correct position
        # Let us sort the left array and right array separately
        quickSort(input, low, partitionIndex - 1)
        quickSort(input, partitionIndex + 1, high)

if __name__ == '__main__':
    input = [4, 1, 3, 7, 9, 8, 2, 6, 5]
    start = timer()
    quickSort(input, 0, len(input) - 1)
    print("Sorted list is {}".format(input))
    end = timer()
    print("Time taken is {}".format(end - start))