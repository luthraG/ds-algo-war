'''
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    Example 1:

    Input: ["flower","flow","flight"]
    Output: "fl"
'''

def longest_common_prefix(str1 = '', str2 = ''):
    length1 = len(str1)
    length2 = len(str2)

    common_prefix = ''

    if length1 > 0 and length2 > 0:
        i = 0
        while i < length1 and i < length2:
            if str1[i] == str2[i]:
                i += 1
            else:
                break
        
        if i > 0:
            common_prefix = str1[:i]
    
    return common_prefix

items = str(input('Enter list of items (separated by comma) :: ')).split(',')
items = list(map(str, items))

common_prefix = items[0]
i = 1
length = len(items)
while i < length:
    common_prefix = longest_common_prefix(common_prefix, items[i])
    i += 1

print('Longest common prefix : {}'.format(common_prefix))