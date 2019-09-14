'''
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    Input: ["flower","flow","flight"]
    Output: "fl"
'''

from timeit import default_timer as timer

def longest_common_prefix(str1 = '', str2 = ''):
    common_prefix = ''

    length1 = len(str1)
    length2 = len(str2)

    if length1 == 0 or length2 == 0:
        return common_prefix
    else:
        i = 0
        while i < length1 and i < length2:
            if str1[i] == str2[i]:
                i += 1
            else:
                break
        
        if i > 0:
            common_prefix = str1[0:i]
    
    return common_prefix

items = str(input('Enter input strings(separated by comma). Press ENTER to stop :: ')).split(',')
items = list(map(str, items))

start = timer()
common_prefix = items[0]

i = 1
length = len(items)

while i < length:
    common_prefix = longest_common_prefix(common_prefix, items[i])
    i += 1

end = timer()
print('Longest common prefix is {}'.format(common_prefix))
print('Time taken is {}'.format(end - start))