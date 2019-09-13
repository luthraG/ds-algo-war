'''
    https://leetcode.com/problems/add-binary/

    Given two binary strings, return their sum (also a binary string).

    The input strings are both non-empty and contains only characters 1 or 0.
'''

binary_maths = {
    '00': {
        'sum': '0',
        'carry': '0'
    },
    '01': {
        'sum': '1',
        'carry': '0'
    },
    '10': {
        'sum': '1',
        'carry': '0'
    },
    '11': {
        'sum': '0',
        'carry': '1'
    }
}

def add_binary(num1, num2):
    sum_of_binary = ''
    length1 = len(num1)
    length2 = len(num2)
    carry = 0

    if length1 > length2:
        num2 = num2.zfill(length1)
    else:
        num1 = num1.zfill(length2)
    i = len(num1) - 1
    while i >= 0:
        sum = int(num1[i]) + int(num2[i])
        if sum == 2:
            if carry == 0:
                carry = 1
                sum_of_binary = '0' + sum_of_binary
            else:
                sum_of_binary = '1' + sum_of_binary
        elif sum == 1:
            if carry == 0:
                sum_of_binary = '1' + sum_of_binary
            else:
                sum_of_binary = '0' + sum_of_binary
        elif sum == 0:
            if carry == 0:
                sum_of_binary = '0' + sum_of_binary
            else:
                carry = 0
                sum_of_binary = '1' + sum_of_binary

        i -= 1
    
    if carry > 0:
        sum_of_binary = '1' + sum_of_binary

    return sum_of_binary

binary1 = str(input('Enter first binary number :: '))
binary2 = str(input('Enter second binary number :: '))

print('Sum of binary numbers is {}'.format(add_binary(binary1, binary2)))
        