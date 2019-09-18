'''
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

'''

def sum_of_two_numbers(nums, target):
    i = 0
    length = len(nums)

    while i < length:
        complement = target - nums[i]

        for x in range(i + 1, length , 1):
            if nums[x] == complement:
                return [i, x]
        
        i += 1
    
    return [-1, -1]