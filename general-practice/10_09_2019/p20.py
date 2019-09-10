'''
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?
'''

from timeit import default_timer as timer

number = int(input('Enter power :: '))

start = timer()
exp = 2 << (number - 1)
sum = 0

while exp != 0:
    sum += (exp % 10)
    exp //= 10

end = timer()
print('Sum of digits of 2 raised to {} is {}'.format(number, sum))
print('Time taken is : {}'.format(end - start))