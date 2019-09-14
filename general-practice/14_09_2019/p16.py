'''
    Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
'''

def lower(input_string: str) -> str:

    i = 0
    length = len(input_string)
    final = ''

    while i < length:
        character = input_string[i]
        ascii_val = ord(character)
        if ascii_val >= 65 and ascii_val <= 91:
            character = chr(ascii_val + 32)
        final += character
        i += 1

    return final

input_string = str(input('Enter the string :: '))
print('Lowercase value of string is : {}'.format(lower(input_string)))
