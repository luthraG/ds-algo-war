'''
    Given a 32-bit signed integer, reverse digits of an integer.

    Example 1:
    Input: 123
    Output: 321

    Example 2:
    Input: -123
    Output: -321

    Example 3:
    Input: 120
    Output: 21

    Note:
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
    [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer
    overflows.
'''

def is_valid(num):
    return -1 * 2** 31 <= num <= 2 ** 31 - 1

def reverse_num(num):
    if is_valid(num):
        is_negative = num < 0
        x = abs(num)

        reverse = 0
        while x:
            x, remainder = divmod(num, 10)
            reverse = reverse * 10 + remainder
        
        reverse = -1 * reverse if is_negative else reverse
        return reverse if is_valid(reverse) else 0
    else:
        return 0
