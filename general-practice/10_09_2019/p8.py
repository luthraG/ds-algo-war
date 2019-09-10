class ArrayStats:
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
    
    def mean(self, items, length):
        sum = 0
        i = 0
        while i < length:
            sum += items[i]
            i += 1
        
        return (sum / length)

if __name__ == '__main__':
    nums = str(input('Enter the numbers(separated by comma). Press ENTER to stop :: ')).split(',')
    nums = list(map(int, nums))
    stats = ArrayStats()
    length = len(nums)
    # stats.bubbleSort(nums, length)
    print('Mean of numbers is {}'.format(stats.mean(nums, length)))