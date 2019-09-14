'''
    Count the number of segments in a string,
    where a segment is defined to be a contiguous sequence of non-space characters.

    Please note that the string does not contain any non-printable characters.
'''

import re

def segments_count(input_string: str) -> int:
    pattern = re.compile(r'[^\s]+\s*')
    matches = re.findall(pattern, input_string)
    return len(matches)

input_string = str(input('Enter the string :: '))
print('Total number of segments in inputted string are : {}'.format(segments_count(input_string)))
