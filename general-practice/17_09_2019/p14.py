'''
    Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

    Note:

    1.The length of both num1 and num2 is < 5100.
    2. Both num1 and num2 contains only digits 0-9.
    3. Both num1 and num2 does not contain any leading zero.
    4. You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''

def add_large_numbers(num1, num2):
    length1 = len(num1)
    length2 = len(num2)

    if length1 > length2:
        num2 = num2.zfill(length1)
    else:
        num1 = num1.zfill(length2)

    i = len(num1) - 1

    overall_sum = ''
    carry = 0

    while i >= 0:
        current_sum = int(num1[i]) + int(num2[i]) + carry
        overall_sum = str(current_sum % 10) + overall_sum
        carry = current_sum // 10
        i -= 1
    
    if carry > 0:
        overall_sum = str(carry) + overall_sum

    return overall_sum

num1, num2 = str(input('Enter two numbers :: ')).split(',')
num1, num2 = str(num1), str(num2)
print('Sum of given numbers is {}'.format(add_large_numbers(num1, num2)))