'''
    Given a non-empty string check if it can be constructed by taking a substring of it and
    appending multiple copies of the substring together.
    You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

    Example 1:

    Input: "abab"
    Output: True
    Explanation: It's the substring "ab" twice.
    Example 2:

    Input: "aba"
    Output: False
    Example 3:

    Input: "abcabcabcabc"
    Output: True
    Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
'''

def can_construct_string(str1):
    length = len(str1)
    i = 1

    limit = length // 2

    while i <= limit:
        times = length // i
        if str1[:i] * times == str1:
            return True
        i += 1
    return False

str1 = str(input('Enter input string :: '))
print('can this string be constructed by sub strings :: {}'.format(can_construct_string(str1)))