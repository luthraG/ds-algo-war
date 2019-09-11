'''
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?
'''

from timeit import default_timer as timer

power = int(input('Enter the power that needs to be raised to base 2 :: '))
start = timer()
sum_of_digits = 0

number = 2 << (power - 1)
number = str(number)
length = len(number)
i = 0
while i < length:
    sum_of_digits += int(number[i])
    i += 1
# while number != 0:
#     sum_of_digits += (number % 10)
#     number //= 10
end = timer()
print('Sum of digits of 2 raised to power {} is {}'.format(power, sum_of_digits))
print('Time taken is {}'.format(end - start))