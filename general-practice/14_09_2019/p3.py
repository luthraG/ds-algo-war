'''
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    An input string is valid if:

    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Note that an empty string is also considered valid.
'''

brackets_map = {
    ')': '(',
    '}': '{',
    ']': '['
}

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedListAsStack:
    def __init__(self):
        self.start_node = Node()
    
    def add_to_start(self, data):
        node = Node(data)
        node.next = self.start_node.next
        self.start_node.next = node
    
    def remove_from_start(self):
        node = self.start_node.next

        if node is not None:
            value = node.data
            self.start_node.next = node.next
            node = None
            return value
        else:
            return -1
    
    def has_any_item(self):
        node = self.start_node.next

        if node is not None:
            return True

        return False

class Solution:
    def is_valid_expression(self, expression = ''):
        stack = LinkedListAsStack()
        valid = True

        length = len(expression)
        if length == 0:
            return valid
        else:
            i = 0
            while i < length:
                item = expression[i]
                if item in '({[':
                    stack.add_to_start(item)
                else:
                    expected = brackets_map[item]
                    while True:
                        removed = stack.remove_from_start()
                        if removed == expected:
                            break
                        else:
                            return False
                i += 1
        if stack.has_any_item():
            valid = False
        return valid

if __name__ == '__main__':
    sol = Solution()
    expression = str(input('Enter expression :: '))
    print('Is inputted expression is valid :: {}'.format(sol.is_valid_expression(expression)))