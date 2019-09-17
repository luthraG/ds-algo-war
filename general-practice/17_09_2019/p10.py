'''
    Write a function that reverses a string. The input string is given as an array of characters char[].

    Do not allocate extra space for another array,
    you must do this by modifying the input array in-place with O(1) extra memory.

    You may assume all the characters consist of printable ascii characters.

    Example 1:

    Input: ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]
    Example 2:

    Input: ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]
'''

def reverse_string(characters):
    length = len(characters)
    i = 0
    limit = length // 2

    while i < limit:
        if characters[i] != characters[length - 1 - i]:
            temp = characters[i]
            characters[i] = characters[length - 1 - i]
            characters[length - 1 - i] = temp
        i += 1

string = str(input('Enter string = '))
string = list(string)
reverse_string(string)
print('Reversed string is {}'.format(string))