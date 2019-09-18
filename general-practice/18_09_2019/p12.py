'''
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    Example 1:
    Input: ["flower","flow","flight"]
    Output: "fl"

    Example 2:
    Input: ["dog","racecar","car"]
    Output: ""

    Explanation: There is no common prefix among the input strings.

    Note:
    All given inputs are in lowercase letters a-z.
'''

def longest_common_prefix(str1, str2):
    length1 = len(str1)
    length2 = len(str2)

    if length1 == 0 or length2 == 0:
        return ''
    else:
        i = 0
        while i < length1 and i < length2:
            if str1[i] != str2[i]:
                break
            
            i += 1

        return str1[0:i] if i > 0 else ''

def longest_common_prefix_solution(items):
    length = len(items)
    common_prefix = items[0] if length > 0 else ''

    i = 1
    while i < length:
        common_prefix = longest_common_prefix(common_prefix, items[i])
        i += 1

    return common_prefix