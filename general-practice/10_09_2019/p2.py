class ArraySetOperations:
    def bubbleSort(self, items, length):
        i = 0
        while i < length:
            j = 0
            while j < length - 1 - i:
                if items[j] > items[j + 1]:
                    items[j + 1] = items[j] + items[j + 1]
                    items[j] = items[j + 1] - items[j]
                    items[j + 1] = items[j + 1] - items[j]
                j += 1
            i += 1
    
    def intersection(self, array1, array2, length1, length2):
        array_intersection = []
        i = 0
        j = 0
        while i < length1 and j < length2:
            if array1[i] < array2[j]:
                i += 1
            elif array1[i] > array2[j]:
                j += 1
            else:
                array_intersection.append(array1[i])
                i += 1
                j += 1
        
        return array_intersection

if __name__ == '__main__':
    arrayOps = ArraySetOperations()
    array1 = str(input('Enter items of first list(separated by comma) = ')).split(',')
    array1 = list(map(int, array1))
    array2 = str(input('Enter items of second list(separated by comma) = ')).split(',')
    array2 = list(map(int, array2))
    length1 = len(array1)
    length2 = len(array2)
    arrayOps.bubbleSort(array1, length1)
    arrayOps.bubbleSort(array2, length2)
    print('Itersection of two sets is : {}'.format(arrayOps.intersection(array1, array2, length1, length2)))
