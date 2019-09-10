'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below N
where 1 <= N <= 10**12
'''

number = int(input('Enter uppewr limit of number :: '))
# Since we need below number
number -= 1

limit_3 = number // 3
limit_5 = number // 5
limit_15 = number // 15

number += 1

sum_3 = (limit_3 * (limit_3 + 1)) // 2
sum_5 = (limit_5 * (limit_5 + 1)) // 2
sum_15 = (limit_15 * (limit_15 + 1)) // 2

sum = 3*sum_3 + 5*sum_5 - 15*sum_15
print('Sum of numbers that are multiple of 3 and 5 below {} are {}'.format(number, sum))
