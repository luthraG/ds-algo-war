'''
    https://leetcode.com/problems/reverse-vowels-of-a-string/

    Write a function that takes a string as input and reverse only the vowels of a string.

    Input: "hello"
    Output: "holle"
'''

vowels = {
    'a': True,
    'e': True,
    'i': True,
    'o': True,
    'u': True
}

def reverse_vowel(input_string):
    vowels = "aeiou"
    items = list(input_string)
    i = 0
    j = len(input_string) - 1

    while i < j:
        if items[i].lower() not in vowels:
            i += 1
        elif items[j].lower() not in vowels:
            j -= 1
        else:
            items[i], items[j] = items[j], items[i]
            i += 1
            j -= 1

    return "".join(items)

input_string = str(input('Enter the string :: '))
print('String with vowels reversed is : {}'.format(reverse_vowel(input_string)))