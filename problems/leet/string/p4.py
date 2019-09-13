'''
    https://leetcode.com/problems/implement-strstr/

    Implement strStr().

    Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    When needle is empty string then return 0
'''

def indexOf(haystack, needle = ''):
    index = -1
    if len(needle) == 0:
        return 0
    else:
        lengthHay = len(haystack)
        lengthNeedle = len(needle)

        i = 0
        limit = lengthHay - lengthNeedle
        while i <= limit:
            found = True
            j = 0
            for x in range(i, i + lengthNeedle, 1):
                if haystack[x] != needle[j]:
                    found = False
                j += 1
            if found:
                index = i
                break
            i += 1

    return index

haystack = str(input('Enter haystack :: '))
needle = str(input('Enter needle :: '))
print('IndexOf needle in haystack :: {}'.format(indexOf(haystack, needle)))
