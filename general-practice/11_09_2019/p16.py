class ArraySetOps:
    def mean(self, items):
        length = len(items)
        sum_of_items = 0
        for item in items:
            sum_of_items += item
        
        return (sum_of_items / length)

if __name__ == '__main__':
    arraySetOps = ArraySetOps()
    numbers = str(input('Enter list of numbers(separated by comma). Press enter to stop :: ')).split(',')
    numbers = list(map(int, numbers))
    print('Mean of numbers is : {}'.format(arraySetOps.mean(numbers)))