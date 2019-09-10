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

    def union(self, array1, array2, length1, length2):
        union_value = []
        handled = {}

        i = 0
        j = 0

        while i < length1 and j < length2:
            if array1[i] < array2[j]:
                value = array1[i]
                if value not in handled:
                    union_value.append(array1[i])
                    handled[value] = True
                i += 1
            elif array2[j] < array1[i]:
                value = array2[j]
                if value not in handled:
                    union_value.append(array2[j])
                    handled[value] = True
                j += 1
            else:
                value = array1[i]
                if value not in handled:
                    union_value.append(array1[i])
                    handled[value] = True
                i += 1
                j += 1

        while i < length1:
            union_value.append(array1[i])
            i += 1

        while j < length2:
            union_value.append(array2[j])
            j += 1

        return union_value
    
if __name__ == '__main__':
    arrayOps = ArraySetOperations()
    array1 = str(input('Enter first list of values(separated by comma) = ')).split(',')
    array1 = list(map(int, array1))
    array2 = str(input('Enter second list of values(separated by comma) = ')).split(',')
    array2 = list(map(int, array2))
    length1 = len(array1)
    length2 = len(array2)
    # let us sort both the lists
    arrayOps.bubbleSort(array1, length1)
    arrayOps.bubbleSort(array2, length2)

    print('Union of two sets is : {}'.format(arrayOps.union(array1, array2, length1, length2)))
