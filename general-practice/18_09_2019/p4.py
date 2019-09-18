'''
    https://leetcode.com/problems/reverse-integer/


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
    [−2^31,  2^31 − 1].
    For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

    Thinking:

    1. Keep on diving the number by 10 and using modulo keep on taking unit place digit
    2. Once number is formed return
    3. Also check the length of number, if it exceeds the boundary values then return 0
    4. If it is equal to boundary value then check unit place digit to see if it is under control or not

    Digits in 2^n is n(log2) + 1 where base is 10
'''


def is_valid(self, num: int) -> bool:
    return -1 * 2**31 <= num <= 2**31 - 1

def reverse(self, num: int) -> int:

    is_negative = num < 0
    x = abs(num)

    if self.is_valid(x) is False:
        return 0

    rev = 0
    while x:
        x, remainder = divmod(x, 10)
        rev = 10 * rev + remainder

    rev = -1 * rev if is_negative else rev
    return rev if self.is_valid(rev) else 0