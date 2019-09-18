'''
    https://leetcode.com/problems/two-sum/

    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

    Thinking:

    sum = a + b
    1. sum is given
    2. First number I know
    3. Sum - first number --> iterates to check second number

    Result:

    Runtime: 3136 ms, faster than 23.07% of Python3 online submissions for Two Sum.
    Memory Usage: 14.9 MB, less than 11.62% of Python3 online submissions for Two Sum.

'''

def sum_of_two_numbers(nums, target):
    i = 0
    length = len(nums)
    idx1 = -1
    idx2 = -1

    while i < length:
        next_num = target - nums[i]
        idx1 = i
        for x in range(i + 1, length, 1):
            if next_num == nums[x]:
                idx2 = x
                break
        if idx2 != -1:
            return [idx1, idx2]
        i += 1

    return [ -1, -1]

numbers = str(input('Enter comma separated numbers :: ')).split(',')
numbers = list(map(int, numbers))
target = int(input('Enter target :: '))

print('Index of numbers that produces the taget :: {}'.format(sum_of_two_numbers(numbers, target)))