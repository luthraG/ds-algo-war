'''
    https://leetcode.com/problems/greatest-common-divisor-of-strings

    For strings S and T, we say "T divides S" if and only if S = T + ... + T 
    (T concatenated with itself 1 or more times)

    Return the largest string X such that X divides str1 and X divides str2.

    Example 1:

    Input: str1 = "ABCABC", str2 = "ABC"
    Output: "ABC"

    Example 2:

    Input: str1 = "ABABAB", str2 = "ABAB"
    Output: "AB"

    Example 3:

    Input: str1 = "LEET", str2 = "CODE"
    Output: ""

'''

def GCD(str1, str2):
    length1 = len(str1)
    length2 = len(str2)

    if length1 > length2:
        num = length1
        den = length2
    else:
        num = length2
        den = length1

    rem = num % den

    while rem != 0:
        num = den
        den = rem
        rem = num % den
    
    return den

def gcdOfStrings(str1, str2):
    gcd = GCD(str1, str2)
    gcd_string = str1[:gcd]

    # Check if it is valid gcd
    l1 = len(str1)
    l2 = len(str2)
    l = len(gcd_string)

    if l1 % l == 0 and l2 % l == 0:
        if ((l1 // l) * gcd_string == str1 and (l2 // l) * gcd_string == str2):
            return gcd_string
        else:
            return ''
    else:
        return ''

str1 = str(input('Enter first string :: '))
str2 = str(input('Enter second string :: '))

print('GCD of strings is {}'.format(gcdOfStrings(str1, str2)))