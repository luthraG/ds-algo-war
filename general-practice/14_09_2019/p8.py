'''
    Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
    return the length of last word in the string.

    If the last word does not exist, return 0.

    Note: A word is defined as a character sequence consists of non-space characters only.
'''

def length_of_last_word(input_string):
    length = 0

    i = len(input_string) - 1
    while i >= 0 :
        if input_string[i] != ' ':
            length += 1
        elif length != 0:
            break
        i -= 1
    
    return length

input_string = str(input('Enter input string :: '))
print('Length of last word of input string is {}'.format(length_of_last_word(input_string)))