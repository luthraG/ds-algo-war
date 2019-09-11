class ArraySetOps:
    def mode(self, items):
        i = 0
        length = len(items)
        hash_map = {}

        highest_freq = -1
        highest_freq_item = items[0]

        while i < length:
            item = items[i]
            if item in hash_map:
                value = hash_map[item] + 1
                hash_map[item] = value
                if value > highest_freq:
                    highest_freq = value
                    highest_freq_item = item
                elif value == highest_freq:
                    if item > highest_freq_item:
                        highest_freq_item = item
            else:
                hash_map[item] = 1

            i += 1
        
        return highest_freq_item

if __name__ == '__main__':
    arraySetOps = ArraySetOps()
    numbers = str(input('Enter list of numbers(separated by comma). Press ENTER when done :: ')).split(',')
    numbers = list(map(int, numbers))
    print('Mode of numbers is {}'.format(arraySetOps.mode(numbers)))