'''
    Given a word, you need to judge whether the usage of capitals in it is right or not.

    We define the usage of capitals in a word to be right when one of the following cases holds:

    1. All letters in this word are capitals, like "USA".
    2. All letters in this word are not capitals, like "leetcode".
    3. Only the first letter in this word is capital, like "Google".
    4. Otherwise, we define that this word doesn't use capitals in a right way.
'''

def is_valid_capital(input_string):
    capital_count = 0
    i = 0
    length = len(input_string)
    if length == 0:
        return False
    while i < length:
        if input_string[i].isupper():
            capital_count += 1
        i += 1
    
    if capital_count == 0 or capital_count == length or (capital_count == 1 and input_string[0].isupper()):
        return True
    
    return False

input_string = str(input('Enter the input string :: '))
print('Is input contains valid capitals :: {}'.format(is_valid_capital(input_string)))
