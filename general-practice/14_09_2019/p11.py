'''
    Given a string,
    find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
'''

def lowest_pos_non_repeating(input_string):
    START_INDEX = 97
    length = len(input_string)
    lowest_pos = -1
    items = [0] * 26

    i = 0
    while i < length:
        items[ord(input_string[i]) - START_INDEX] += 1
        i += 1
    
    i = 0
    while i < 26:
        if items[i] == 1:
            pos = input_string.index(chr(i + START_INDEX))
            if pos < lowest_pos or lowest_pos == -1:
                lowest_pos = pos
                if lowest_pos == 0:
                    break
        i += 1

    return lowest_pos

input_string = str(input('Enter string to find lowest non repeating character :: '))
print('Lowest position of non-repeating character is {}'.format(lowest_pos_non_repeating(input_string)))