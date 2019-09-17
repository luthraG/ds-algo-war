'''
    Given a word, you need to judge whether the usage of capitals in it is right or not.

    We define the usage of capitals in a word to be right when one of the following cases holds:

    1. All letters in this word are capitals, like "USA".
    2. All letters in this word are not capitals, like "leetcode".
    3. Only the first letter in this word is capital, like "Google".
    4. Otherwise, we define that this word doesn't use capitals in a right way.
    

    Example 1:

    Input: "USA"
    Output: True
    

    Example 2:

    Input: "FlaG"
    Output: False
'''

def is_valid_capital(str1):
    i = 0
    length = len(str1)
    capital_count = 0

    while i < length:
        if str1[i] == str1[i].upper():
            capital_count += 1
        i += 1
    
    if capital_count == 0 or capital_count == length or (capital_count == 1 and str1[0] == str1[0].upper()):
        return True
    else:
        return False

str1 = str(input('Enter string = '))
print('Does input string contains valid capitals :: {}'.format(is_valid_capital(str1)))
