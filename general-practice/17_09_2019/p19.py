'''
    Implement function ToUpperCase() that has a string parameter str, and returns the same string in uppercase.
 
'''

def to_upper(str1):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    i = 0
    length = len(str1)

    while i < length:
        char = str1[i]
        if char in lower:
            str1[i] = chr(ord(char) - 32)
        i += 1

str1 = list(str(input('Enter the string to be converted to upper case :: ')))
to_upper(str1)
print('Upper case version of input string is {}'.format(''.join(str1)))