class ArrayStats:
    def mode(self, items, length):
        i = 0
        highest_count = -1
        highest_count_item = items[0]
        hash_map = {}
        while i < length:
            item = items[i]
            if item in hash_map:
                value = hash_map[item] + 1
                if value > highest_count:
                    highest_count = value
                    highest_count_item = item
                hash_map[item] = value
            else:
                value = 1
                hash_map[item] = value
            i += 1

        return highest_count_item

if __name__ == '__main__':
    nums = str(input('Enter the numbers(separated by comma). Press ENTER to stop :: ')).split(',')
    nums = list(map(int, nums))
    stats = ArrayStats()
    length = len(nums)
    print('Mode of numbers is {}'.format(stats.mode(nums, length)))