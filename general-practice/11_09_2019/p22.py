import operator
import re

ops = {
    '+': operator.add,
    '-': operator.sub
}

expression = str(input('Enter mathematical expression(containing pluses and minues) :: '))

pattern = re.compile(r'([0-9])+([+-])*')

operation = None
stack = 1

for number, op in re.findall(pattern, expression):
    if operation:
        stack = operation(int(stack), int(number))
    
    if op:
        operation = ops[op]
    
    if operation is None:
        stack = number

print('Expression value is {}'.format(stack))