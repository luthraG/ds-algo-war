class ArraySetOps:
    def intersection(self, list1, list2):
        length1 = len(list1)
        length2 = len(list2)

        i = 0
        j = 0

        list_intersection = []

        while i < length1 and j < length2:
            if list1[i] < list2[j]:
                i += 1
            elif list1[i] > list2[j]:
                j += 1
            else:
                list_intersection.append(list1[i])
                i += 1
                j += 1
        
        return list_intersection

if __name__ == '__main__':
    arraySetOps = ArraySetOps()
    items1 = str(input('Enter items in first list(separated by comma). Press ENTER to stop :: ')).split(',')
    items2 = str(input('Enter items in second list(separated by comma). Press ENTER to stop :: ')).split(',')
    items1 = list(map(int, items1))
    items2 = list(map(int, items2))
    print('Union of two sets is {}'.format(arraySetOps.intersection(items1, items2)))
