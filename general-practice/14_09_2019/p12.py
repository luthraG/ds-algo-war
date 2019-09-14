'''
    Given a string, sort it in decreasing order based on the frequency of characters.

    Input:
    "tree"

    Output:
    "eert"
'''

def sort_by_frequency(input_string):
    result = ''
    characters_map = {}

    i = 0
    length = len(input_string)

    while i < length:
        char = input_string[i]
        if char in characters_map:
            characters_map[char] += 1
        else:
            characters_map[char] = 1
        i += 1
    
    items = []
    for key, value in characters_map.items():
        items.append((key, value))
    
    items.sort(key = lambda x: x[1], reverse = True)

    for item in items:
        if item[1]:
            result += (item[0] * item[1])
    
    return result

input_string = str(input('Enter input string :: '))
print('Sorted string based on frequency is : {}'.format(sort_by_frequency(input_string)))