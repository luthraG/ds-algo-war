'''
    https://leetcode.com/problems/length-of-last-word/

    Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
    return the length of last word in the string.

    If the last word does not exist, return 0.

    Note: A word is defined as a character sequence consists of non-space characters only.
'''

from timeit import default_timer as timer

input_string = str(input('Enter the string :: '))
start = timer()

last_word_length = 0
length = len(input_string) - 1
i = length
while i >= 0:
    if input_string[i] != ' ':
        last_word_length += 1
    elif input_string[i] == ' ' and last_word_length > 0:
        break
    i -= 1

end = timer()
print('Length of last word is :: {}'.format(last_word_length))
print('Time taken is {}'.format(end - start))