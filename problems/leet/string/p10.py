'''
    https://leetcode.com/problems/detect-capital/

    Given a word, you need to judge whether the usage of capitals in it is right or not.

    We define the usage of capitals in a word to be right when one of the following cases holds:

    1. All letters in this word are capitals, like "USA".
    2. All letters in this word are not capitals, like "leetcode".
    3. Only the first letter in this word is capital, like "Google".
    4. Otherwise, we define that this word doesn't use capitals in a right way.
    
'''

def is_valid_capital(input_string):
    i = 0
    length = len(input_string)
    capitals_count = 0
    is_first_capital = False

    while i < length:
        if input_string[i].isupper():
            capitals_count += 1
            if i == 0:
                is_first_capital = True
        i += 1

    if capitals_count == length or capitals_count == 0 or (capitals_count == 1 and is_first_capital):
        return True
    else:
        return False

input_string = str(input('Enter valid input string :: '))
print('Is input string using capitals correctly :: {}'.format(is_valid_capital(input_string)))