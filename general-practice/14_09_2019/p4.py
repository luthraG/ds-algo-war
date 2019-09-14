'''
    Implement strStr().

    Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

def indexOf(haystack, needle):
    length1 = len(haystack)
    lenght2 = len(needle)

    if lenght2 == 0:
        return 0
    elif lenght2 > length1:
        return -1
    else:
        i = 0
        limit = length1 - lenght2

        while i <= limit:
            j = 0
            matchFound = True
            for x in range(i, i + lenght2, 1):
                if haystack[x] != needle[j]:
                    matchFound = False
                
                if matchFound is False:
                    break
                j += 1

            if matchFound:
                return i

            i += 1
    return -1

haystack = str(input('Enter haystack :: '))
needle = str(input('Enter needle :: '))

print('Index of {} in {} is {}'.format(needle, haystack, indexOf(haystack, needle)))