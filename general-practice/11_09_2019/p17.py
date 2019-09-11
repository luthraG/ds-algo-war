class ArraySetOps:
    def bubble_sort(self, items, length):
        i = 0
        while i < length:
            j = 0
            while j < length - 1 - i:
                if items[j] > items[j + 1]:
                    items[j + 1] = items[j] + items[j + 1]
                    items[j] = items[j + 1] - items[j]
                    items[j + 1] = items[j + 1] - items[j]
                j += 1
            i +=1
    
    def median(self, items, length):
        if length & 1 == 1:
            return float(items[length // 2])
        else:
            return (items[length // 2] + items[length//2 - 1]) / 2

if __name__ == '__main__':
    arraySetOps = ArraySetOps()
    numbers = str(input('Enter list of numbers(separated by comma). Press ENTER to stop :: ')).split(',')
    numbers = list(map(int, numbers))
    length = len(numbers)
    arraySetOps.bubble_sort(numbers, length)
    print('Median of numbers is {}'.format(arraySetOps.median(numbers, length)))
