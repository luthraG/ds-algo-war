from timeit import default_timer as timer

word_number_map = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '10': 'Ten',
    '11': 'Eleven',
    '12': 'Twelve',
    '13': 'Thirteen',
    '14': 'Fourteen',
    '15': 'Fifteen',
    '16': 'Sixteen',
    '17': 'Seventeen',
    '18': 'Eighteen',
    '19': 'Nineteen',
    '10X2': 'Twenty',
    '10X3': 'Thirty',
    '10X4': 'Fourty',
    '10X5': 'Fifty',
    '10X6': 'Sixty',
    '10X7': 'Seventy',
    '10X8': 'Eighty',
    '10X9': 'Ninty',
    '100': 'Hundred',
    '1000': 'One Thousand'
}


def getName(number):
    numArray = []
    name = ""
    separator = ""

    while number != 0:
        numArray.append(str(number % 10))
        number = number // 10
    numArray.reverse()

    if len(numArray) == 1:
        name = word_number_map[numArray[0]]
    elif len(numArray) == 2:
        if numArray[0] == '1':
            name = word_number_map[numArray[0] + numArray[1]]
        else:
            name = word_number_map['10X' + numArray[0]]
            if (numArray[1] != '0'):
                name = name + separator + word_number_map[numArray[1]]
    elif len(numArray) == 3:
        name = word_number_map[numArray[0]] + separator + word_number_map['100']
        if numArray[1] == '1':
            name = name + separator + 'and' + separator + word_number_map[numArray[1] + numArray[2]]
        elif numArray[1] == '0' and numArray[2] != '0':
            name = name + separator + 'and' + separator + word_number_map[numArray[2]]
        elif numArray[1] == '0' and numArray[2] == '0':
            pass
        else:
            name = name + separator + 'and' + separator + word_number_map['10X' + numArray[1]]
            if (numArray[2] != '0'):
                name = name + separator + word_number_map[numArray[2]]
    elif len(numArray) == 4:
        name = word_number_map['1000']

    return name

if __name__ == '__main__':
    start = timer()
    total_length = 0
    # name = getName(107)
    # print("Name for number is {}".format(name))
    for number in range(1, 1001):
        name = getName(number)
        total_length = total_length + len(name)
        print("Name for number {} is {}".format(number, name))
    print("Total length for name is {}".format(total_length))
    end = timer()
    print("Time taken is {}".format(end - start))
