'''
    Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

    Note:

    1. The length of both num1 and num2 is < 5100.
    2. Both num1 and num2 contains only digits 0-9.
    3. Both num1 and num2 does not contain any leading zero.
    4. You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''

def sum_of_large_numbers(num1, num2):
    length1 = len(num1)
    length2 = len(num2)

    if length1 > length2:
        num2 = num2.zfill(length1)
    else:
        num1 = num1.zfill(length2)
    
    sum_of_numbers = ''
    carry = 0

    i = len(num1) - 1
    while i >= 0:
        sum = int(num1[i]) + int(num2[i]) + carry
        sum_of_numbers = str(sum % 10) + sum_of_numbers
        carry = sum // 10
        i -= 1
    
    if carry > 0:
        sum_of_numbers = str(carry) + sum_of_numbers
    
    return sum_of_numbers

num1 = str(input('Enter first number :: '))
num2 = str(input('Enter second number :: '))

print('Sum of numbers is {}'.format(sum_of_large_numbers(num1, num2)))