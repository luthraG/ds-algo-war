'''
    Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

    Note: For the purpose of this problem, we define empty string as valid palindrome.
'''

def is_palindrome(input_string: str) -> bool:
    alphanumeric = 'abcdefghijklmnopqrstuvwxyz0123456789'
    if len(input_string) == 0:
        return True
    input_string = input_string.lower()
    i = 0
    j = len(input_string) - 1
    
    while i < j:
        if input_string[i] not in alphanumeric:
            i += 1
        elif input_string[j] not in alphanumeric:
            j -= 1
        else:
            if input_string[i] != input_string[j]:
                return False
            else:
                i += 1
                j -= 1
    
    return True

input_string = str(input('Enter the string :: '))
print('Inputted string is palindrome :: {}'.format(is_palindrome(input_string)))