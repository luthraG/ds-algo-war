class ArraySetOps:
    def bubble_sort(self, items):
        length = len(items)
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

    def union(self, list1, list2):
        length1 = len(list1)
        length2 = len(list2)

        union_items = []

        i = 0
        j = 0

        items_added = {}

        while i < length1 and j < length2:
            if list1[i] < list2[j]:
                value = list1[i]
                if value not in items_added:
                    union_items.append(value)
                    items_added[value] = True
                i += 1
            elif list1[i] > list2[j]:
                value = list2[j]
                if value not in items_added:
                    union_items.append(value)
                    items_added[value] = True
                j += 1
            else:
                value = list1[i]
                if value not in items_added:
                    union_items.append(value)
                    items_added[value] = True
                i += 1
                j += 1
        
        while i < length1:
            value = list1[i]
            if value not in items_added:
                union_items.append(value)
                items_added[value] = True
            i += 1
        
        while j < length2:
            value = list2[j]
            if value not in items_added:
                union_items.append(value)
                items_added[value] = True
            j += 1

        return union_items

if __name__ == '__main__':
    arraySetOps = ArraySetOps()
    items1 = str(input('Enter items in first list(separated by comma). Press ENTER to stop :: ')).split(',')
    items2 = str(input('Enter items in second list(separated by comma). Press ENTER to stop :: ')).split(',')
    items1 = list(map(int, items1))
    items2 = list(map(int, items2))
    print('Union of two sets is {}'.format(arraySetOps.union(items1, items2)))
