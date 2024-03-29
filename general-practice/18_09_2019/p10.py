'''
    Determine whether an integer is a palindrome.
    An integer is a palindrome when it reads the same backward as forward.

    Example 1:
    Input: 121
    Output: true

    Example 2:
    Input: -121
    Output: false

    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
    
    Example 3:
    Input: 10
    Output: false

    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

    Follow up:
    Coud you solve it without converting the integer to a string?

    Runtime: 80 ms, faster than 36.74% of Python3 online submissions for Palindrome Number.
    Memory Usage: 14.1 MB, less than 6.50% of Python3 online submissions for Palindrome Number.

'''

# Without converting number to string
def is_palindrome(num):
    if num < 0:
        return False
    else:
        reverse = 0
        x = num
        while x:
            remainder = x % 10
            reverse = 10 * reverse + remainder
            x //= 10

        return num == reverse

