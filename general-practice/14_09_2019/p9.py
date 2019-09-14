'''
    Given two binary strings, return their sum (also a binary string).

    The input strings are both non-empty and contains only characters 1 or 0.
'''

def add_binary(bin1, bin2):
    sum_of_binaries = ''

    length1 = len(bin1)
    length2 = len(bin2)

    if length1 > length2:
        bin2 = bin2.zfill(length1)
    else:
        bin1 = bin1.zfill(length2)
    
    i = len(bin1) - 1
    carry = '0'

    while i >= 0:
        a = int(bin1[i])
        b = int(bin2[i])

        sum = a + b
        if sum == 2:
            if carry == '1':
                sum_of_binaries = '1' + sum_of_binaries
            else:
                sum_of_binaries = '0' + sum_of_binaries
                carry = '1'
        elif sum == 1:
            if carry == '1':
                sum_of_binaries = '0' + sum_of_binaries
            else:
                sum_of_binaries = '1' + sum_of_binaries
        elif sum == 0:
            if carry == '1':
                sum_of_binaries = '1' + sum_of_binaries
                carry = '0'
            else:
                sum_of_binaries = '0' + sum_of_binaries
        i -= 1
    
    if carry == '1':
        sum_of_binaries = carry + sum_of_binaries

    return sum_of_binaries

bin1, bin2 = str(input('Enter two binary numbers(separated by comma) :: ')).split(',')
print('Sum of binary numbers is : {}'.format(add_binary(bin1, bin2)))