'''
    Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
 
    Example 1:

    Input: "Hello"
    Output: "hello"
    Example 2:

    Input: "here"
    Output: "here"
    Example 3:

    Input: "LOVELY"
    Output: "lovely"
'''

def to_lower(str1):
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    i = 0
    length = len(str1)

    while i < length:
        char = str1[i]
        if char in upper:
            char = chr(ord(char) + 32)
        str1[i] = char
        i += 1

str1 = list(str(input('Enter the string to be converted to lower case :: ')))
to_lower(str1)
print('Lowercase form of input is {}'.format(''.join(str1)))