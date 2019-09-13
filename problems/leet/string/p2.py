'''
    https://leetcode.com/problems/longest-common-prefix/

    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    Note: All given inputs are in lowercase letters a-z.
'''

from timeit import default_timer as timer

def largest_common_prefix(item1 = '', item2 = ''):
    print('item1 : {} and item2: {}'.format(item1, item2))
    common_prefix = ''
    if item1 == '' or item2 == '':
        common_prefix = ''
    else:
        length1 = len(item1)
        length2 = len(item2)

        i = 0
        while i < length1 and i < length2:
            if item1[i] == item2[i]:
                i += 1
            else:
                break
        
        if i > 0:
            common_prefix = item1[0:i]

    return common_prefix

items = str(input('Enter the items(comma separated). Press ENTER to stop :: ')).split(',')
items = list(map(str, items))
start = timer()
common_prefix = ''
i = 1
length = len(items)
if length > 0:
    common_prefix = items[0]
while i < length:
    common_prefix = largest_common_prefix(common_prefix, items[i])
    i += 1
end = timer()
print('Largest common prefix amongst list of strings :: {}'.format(common_prefix))
print('Time taken is {}'.format(end - start))