class BubbleSort:
    def sort(self, items):
        i = 0
        length = len(items)
        while i < length:
            j = 0
            while j < length - 1 - i:
                if items[j] > items[j + 1]:
                    temp = items[j + 1]
                    items[j + 1] = items[j]
                    items[j] = temp
                j += 1
            i += 1
    
if __name__ == '__main__':
    bubbleSort = BubbleSort()
    numbers = str(input('Enter numbers(separated by comma) to be sorted(Press enter when done) :: ')).split(',')
    numbers = [int(number) for number in numbers]
    bubbleSort.sort(numbers)
    print('Sorted values are : {}'.format(numbers))