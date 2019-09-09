class Algebra:
    def sort(self, items, length):
        i = 0
        while i < length:
            j = 0
            while j < length - 1 - i:
                if items[j] > items[j + 1]:
                    items[j + 1] = items[j + 1] + items[j]
                    items[j] = items[j + 1] - items[j]
                    items[j + 1] = items[j + 1] - items[j]
                j += 1
            i += 1

    def median(self, items, length):
        # Let us first sort the items
        self.sort(items, length)

        # If number of items are odd
        # then take the middle element
        if length & 1 == 1:
            return float(items[length // 2])
        else:
            # If number of items are even
            # then take average of middle two elements
            return ((items[length // 2] + items[length // 2 - 1]) / 2)

if __name__ == '__main__':
    algebra = Algebra()
    numbers = str(input('Enter the numbers(separated by comma) and press enter when done :: ')).split(',')
    numbers = [int(number) for number in numbers]
    length = len(numbers)
    print('median of numbers is {}'.format(algebra.median(numbers, length)))
