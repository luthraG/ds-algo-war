'''
    Given a string, find the first non-repeating character in it and return it's index.
    If it doesn't exist, return -1.

    Examples:

    s = "leetcode"
    return 0.

    s = "loveleetcode",
    return 2.
    Note: You may assume the string contain only lowercase letters.

'''

def non_repeating_character(string):
    length = len(string)
    characters = [0] * 26
    START_INDEX = 97
    lowest_pos = length

    i = 0
    while i < length:
        characters[ord(string[i]) - START_INDEX] += 1
        i += 1

    i = 0
    while i < 26:
        if characters[i] == 1:
            char = chr(i + START_INDEX)
            pos = string.index(char)
            if pos < lowest_pos:
                lowest_pos = pos
        i += 1

    return lowest_pos if lowest_pos != length else -1

str1 = str(input('Enter string = '))
print('Position of first non repeating character is {}'.format(non_repeating_character(str1)))