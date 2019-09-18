'''
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    An input string is valid if:

    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Note that an empty string is also considered valid.

    Example 1:
    Input: "()"
    Output: true

    Example 2:
    Input: "()[]{}"
    Output: true

    Example 3:
    Input: "(]"
    Output: false

    Example 4:
    Input: "([)]"
    Output: false

    Example 5:
    Input: "{[]}"
    Output: true
'''

brackets_map = {
    ']' : '[',
    '}' : '{',
    ')': '('
}

def is_valid_brackets(expression):
    i = 0
    length = len(expression)

    stack = []

    while i < length:
        item = expression[i]
        if item in '({[':
            stack.append(item)
        else:
            expected = brackets_map[item]
            removed = stack.pop() if stack else None
            if removed != expected:
                return False
        i += 1

    return True if len(stack) == 0 else False