'''
    Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
    return the length of last word in the string.

    If the last word does not exist, return 0.

    Note: A word is defined as a character sequence consists of non-space characters only.

    Example:

    Input: "Hello World"
    Output: 5
'''

def length_of_last_word(str):
    i = len(str) - 1
    count = 0

    while i >= 0:
        if str[i] != ' ':
            count += 1
        elif count != 0:
            break
        i -= 1
    return count

string = str(input('Enter the string = '))
print('Length of last word of {} is {}'.format(string, length_of_last_word(string)))