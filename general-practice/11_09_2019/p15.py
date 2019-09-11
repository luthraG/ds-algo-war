class Sort:
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

if __name__ == '__main__':
    sort = Sort()
    numbers = str(input('Enter the list of numbers(separated by comma). Press enter to stop :: ')).split(',')
    numbers = list(map(int, numbers))
    sort.bubble_sort(numbers)
    print('Sorted list is : {}'.format(numbers))
