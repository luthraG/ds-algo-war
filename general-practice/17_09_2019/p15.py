'''
    Count the number of segments in a string,
    where a segment is defined to be a contiguous sequence of non-space characters.

    Please note that the string does not contain any non-printable characters.

    Example:

    Input: "Hello, my name is John"
    Output: 5

'''

import re

def num_segments(str1):
    pattern = re.compile(r'[^\s]+\s*')
    matches = re.findall(pattern, str1)
    return len(matches)

str1 = str(input('Enter string = '))
print('Total number of segments for given string = {}'.format(num_segments(str1)))