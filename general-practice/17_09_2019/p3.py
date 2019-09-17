'''
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    An input string is valid if:

    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Note that an empty string is also considered valid.

'''

brackets_map = {
    ']': '[',
    '}': '{',
    ')': '('
}

def is_valid_brackets(expression):
    length = len(expression)
    i = 0
    stack = []
    while i < length:
        item = expression[i]
        if item in '({[':
            stack.append(item)
        else:
            open_bracket = brackets_map[item]
            removed = stack.pop() if stack else False
            if removed != open_bracket:
                return False
        i += 1
    
    return False if len(stack) > 0 else True

expression = str(input('Enter expression :: '))
print('Is expression with valid brackets :: {}'.format(is_valid_brackets(expression)))