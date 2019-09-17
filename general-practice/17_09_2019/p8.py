'''
    Given two binary strings, return their sum (also a binary string).

    The input strings are both non-empty and contains only characters 1 or 0.

    Example 1:

    Input: a = "11", b = "1"
    Output: "100"

'''

def add_binaries(bin1, bin2):
    length1 = len(bin1)
    length2 = len(bin2)

    if length1 > length2:
        bin2 = bin2.zfill(length1)
    else:
        bin1 = bin1.zfill(length2)

    i = len(bin1) - 1
    carry = 0
    sum_of_binaries = ''

    while i >= 0:
        sum_of_units = int(bin1[i]) + int(bin2[i])
        if sum_of_units == 2:
            if carry:
                sum_of_binaries = '1' + sum_of_binaries
            else:
                sum_of_binaries = '0' + sum_of_binaries
                carry = 1
        elif sum_of_units == 1:
            if carry:
                sum_of_binaries = '0' + sum_of_binaries
            else:
                sum_of_binaries = '1' + sum_of_binaries
        elif sum_of_units == 0:
            if carry:
                sum_of_binaries = '1' + sum_of_binaries
                carry = 0
            else:
                sum_of_binaries = '0' + sum_of_binaries

        i -= 1
    sum_of_binaries = '1' + sum_of_binaries if carry else sum_of_binaries
    return sum_of_binaries

bin1,bin2 = str(input('Enter two binaries(separated by comma) = ')).split(',')
bin1,bin2 = str(bin1), str(bin2)
print('Sum of binaries is {}'.format(add_binaries(bin1, bin2)))