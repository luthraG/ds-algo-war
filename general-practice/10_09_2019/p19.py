'''
    Work out the first ten digits of the sum of the following N 50-digit numbers.
'''

from timeit import default_timer as timer

total_numbers = int(input('Enter the maximum number of 50 digits numbers :: '))
numbers = []
for i in range(total_numbers):
    numbers.append(str(input('Enter number :: ')))

start = timer()

pos = len(numbers[0]) - 1
sum = 0
carry = 0
answer = ''

while pos >= 0:
    i = 0
    sum = carry
    while i < total_numbers:
        sum += int(numbers[i][pos])
        i += 1
    answer = str(sum % 10) + answer
    carry = sum // 10
    pos -= 1

if carry > 0:
    answer = str(carry) + answer

end = timer()
print('First ten digits in sum are : {}'.format(answer[0:10]))
print('Time taken is : {}'.format(end - start))