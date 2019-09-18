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

    Runtime: 96 ms, faster than 12.44% of Python3 online submissions for Palindrome Number.
    Memory Usage: 14.2 MB, less than 6.50% of Python3 online submissions for Palindrome Number.

'''

# First try with converting number to string
def is_palindrome(num):
    num = str(num)
    if num[0] == '-':
        return False
    else:
        i = 0
        length = len(num)
        limit = length // 2
        while i <= limit:
            if num[i] != num[length - 1 - i]:
                return False
            i += 1

        return True
