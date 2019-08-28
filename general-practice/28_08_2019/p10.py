from timeit import default_timer as timer

if __name__ == '__main__':
    number_of_lines = int(input('Enter the number of lines :: '))
    nums = []
    for num in range(number_of_lines):
        nums.append(str(input('Enter line :: ')))
    
    start = timer()
    one_line_length = len(nums[0])
    carry = 0
    final = ''

    pos = one_line_length - 1

    while pos >= 0:
        total = 0 + carry
        for i in range(0, number_of_lines, 1):
            total += int(nums[i][pos])
        final = str(total % 10) + final
        carry = total // 10
        pos -= 1

    if carry > 0:
        final = str(carry) + final

    print('First ten digits are {}'.format(final[0:10]))
    end = timer()
    print('Time taken is {}'.format(end - start))
    
