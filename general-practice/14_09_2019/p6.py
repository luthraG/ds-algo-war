'''
    Given a non-empty string check if it can be constructed by taking a substring of it
    and appending multiple copies of the substring together.
    You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

    Input: "abab"
    Output: True
    Explanation: It's the substring "ab" twice.

    Input: "aba"
    Output: False
'''

# Idea here is : For a pattern to occur all characters must be present equal number of times
# aaabbb --> This breaks the idea or abccba --> abc cba
# which means you need somthing along with it
# 
def is_repeated_substring(input_string):
    i = 1
    length = len(input_string)
    while i < length:
        if length % i == 0:
            pattern = input_string[:i]
            times = length // i
            if pattern * times == input_string:
                return True
        
        i += 1
    
    return False

input_string = str(input('Enter input string :: '))
print('Can this string be formed by repeating its patterns :: {}'.format(is_repeated_substring(input_string)))
