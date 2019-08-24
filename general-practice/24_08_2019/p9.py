# coding: utf8
'''
    Work out the first ten digits of the sum of N, 50 digits  numbers.

    Input Format

    First line contains N, next N lines contain a 50 digit number each.

    Constraints
    1 <= N <= 1000

    Output Format

    Print only first 10 digit of the final sum
'''

if __name__ == '__main__':
    total_numbers = int(input())
    numbers = []
    for idx in range(total_numbers):
        numbers.append(str(input()))
    
    ret = ''
    carry = 0
    position = len(numbers[0]) - 1

    while position > -1:
        idx = 0
        sum = 0
        while idx < total_numbers:
            sum += int(numbers[idx][position])
            idx += 1
        
        sum += carry
        # compute carry for next column and number to return
        ret = str(sum % 10) + ret
        carry = sum // 10
        
        # Let us move to next column
        position -= 1
    
    if carry > 0:
        ret = str(carry) + ret
    
    print(ret[0: 10])
