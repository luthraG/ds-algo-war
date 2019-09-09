import re
import operator

ops = {
    '+': operator.add,
    '-': operator.sub
}

expression = input('Enter expression = ')
pattern = re.compile(r'([0-9]+)([+-])*')


stack = None
operation = None
for number, op in re.findall(pattern, expression):
    if operation:
        stack = operation(int(stack), int(number))
    if op:
        operation = ops[op]
    if stack is None:
        stack = number

print(stack)
