'''
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

'''

def sum_of_numbers(nums, target):
    i = 0
    length = len(nums)

    complement_dict = {}

    while i < length:
        complement = target - nums[i]

        if complement in complement_dict:
            return [complement_dict[complement], i]
        else:
            complement_dict[nums[i]] = i

