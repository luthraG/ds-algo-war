import operator
import re

ops = {
    '+': operator.add,
    '-': operator.sub
}

pattern = re.compile(r'([0-9]+)([+-]*)')

expression = str(input('Enter mathematical expression containing plueses and minues :: '))

stack = 0
operation = None

for number, operator in re.findall(pattern, expression):
    if operation:
        stack = operation(int(stack), int(number))

    if operation is None:
        stack = number
    
    if operator:
        operation = ops[operator]

print('Expression resolves to : {}'.format(stack))