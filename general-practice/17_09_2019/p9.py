'''
    Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

    Note: For the purpose of this problem, we define empty string as valid palindrome.

    Example 1:

    Input: "A man, a plan, a canal: Panama"
    Output: true
    Example 2:

    Input: "race a car"
    Output: false

'''

def is_palindrome(str1):
    length = len(str1)
    alphanumeric = 'abcdefghijklmnopqrstuvwxyz0123456789'

    if length == 0:
        return True
    else:
        str1 = str1.lower()
        i = 0
        j = length - 1

        while j > i:
            character_i = str1[i]
            character_j = str1[j]

            if character_i not in alphanumeric:
                i += 1
            elif character_j not in alphanumeric:
                j -= 1
            else:
                if character_i == character_j:
                    i += 1
                    j -= 1
                else:
                    return False
        
        return True

string = str(input('Enter the input string = '))
print('Is input string palindrome :: {}'.format(is_palindrome(string)))