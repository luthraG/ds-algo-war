import operator
import re

ops = {
    '+': operator.add,
    '-': operator.sub
}

stack = 0
operation = None

if __name__ == '__main__':
    expression = input('Enter the expression :: ')
    pattern = re.compile(r'([0-9]+)([+-]*)')
    for number, op in re.findall(pattern, expression):
        if operation:
            stack = operation(int(stack), int(number))
        else:
            if number:
                stack = number
        if op:
            operation = ops[op]
    
    print(stack)