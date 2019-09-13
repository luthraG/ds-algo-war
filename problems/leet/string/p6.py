'''
    https://leetcode.com/problems/reverse-string/

    Write a function that reverses a string. The input string is given as an array of characters char[].

    Do not allocate extra space for another array,
    you must do this by modifying the input array in-place with O(1) extra memory.

    You may assume all the characters consist of printable ascii characters.
'''

def reverseString(items):
    length = len(items)
    limit = length // 2
    i = 0
    while i < limit:
        if items[i] != items[length - 1 - i]:
            items[i] = ord(items[i])
            items[length - 1 - i] = ord(items[length - 1 - i])
            items[length - 1 - i] = items[i] + items[length - 1 - i]
            items[i] = items[length - 1 - i] - items[i]
            items[length - 1 - i] = chr(items[length - 1 - i] - items[i])
            items[i] = chr(items[i])
        i += 1

input_str = str(input('Enter input string :: '))
chars = list(input_str)
reverseString(chars)
print('Reverse of string is : {}'.format(chars))