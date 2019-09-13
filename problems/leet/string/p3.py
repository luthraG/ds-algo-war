'''
    https://leetcode.com/problems/valid-parentheses/

    Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid
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
        ret_val = -1001

        if node is not None:
            self.start_node.next = node.next
            ret_val = node.data
            node = None
        
        return ret_val


    def has_any_item(self):
        node = self.start_node.next

        while node is not None:
            if node.data is not None:
                return True
            node = node.next

        return False

class Solution:
    def is_valid(self, expression):
        valid = True
        stack = LinkedListAsStack()

        for item in expression:
            if item in ['(', '{', '[']:
                stack.add_to_start(item)
            else:
                encounter = brackets_map[item]
                # We need to remove from stack till its open is found
                while True:
                    removed = stack.remove_from_start()
                    if removed == -1001:
                        return False
                    elif removed != encounter:
                        return False
                    elif removed == encounter:
                        break

        if stack.has_any_item():
            valid = False
        return valid

if __name__ == '__main__':
    sol = Solution()
    expression = str(input('Enter expression(press ENTER to stop) :: '))
    print('Is expression valid :: {}'.format(sol.is_valid(expression)))
