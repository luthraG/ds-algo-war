'''
    https://leetcode.com/problems/two-sum/

    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

    Thinking:
    Let's try to do it in O(N)

    1. We will maintain a dictionary that will contain the element as key and index as value
    2. During iteration, it does target - num[i] and check if that is in dictionary
    3. If no, then store number as key and index as value and move to next element
    4. If yes, then then fetch it from dictionary

    Result:
    Runtime: 60 ms, faster than 68.96% of Python3 online submissions for Two Sum.
    Memory Usage: 15 MB, less than 7.44% of Python3 online submissions for Two Sum.

'''


def sum_of_two_numbers(nums, target):
    i = 0
    length = len(nums)

    complement_dict = {}
    while i < length:
        complement = target - nums[i]
        if complement in complement_dict:
            return [complement_dict[complement], i]
        else:
            complement_dict[nums[i]] = i
        i += 1

numbers = str(input('Enter comma separated numbers :: ')).split(',')
numbers = list(map(int, numbers))
target = int(input('Enter target sum = '))

print('Index of sum of numbers is {}'.format(sum_of_two_numbers(numbers, target)))