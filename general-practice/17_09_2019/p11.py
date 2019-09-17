'''
    Write a function that takes a string as input and reverse only the vowels of a string.

    Example 1:

    Input: "hello"
    Output: "holle"
    Example 2:

    Input: "leetcode"
    Output: "leotcede"
    Note:
    The vowels does not include the letter "y".


'''

def reverse_vowels(str1):
    length = len(str1)
    i = 0
    j = length - 1

    vowel = 'aeiou'

    while i < j:
        character_i = str1[i]
        character_j = str1[j]

        if character_i not in vowel:
            i += 1
        elif character_j not in vowel:
            j -= 1
        else:
            str1[i] = character_j
            str1[j] = character_i
            i += 1
            j -= 1

string1 = str(input('Enter string :: '))
string1 = list(string1)
reverse_vowels(string1)
print('String with reversed vowels is {}'.format(''.join(string1)))