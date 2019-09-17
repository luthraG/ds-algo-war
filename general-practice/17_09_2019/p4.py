'''
    Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    when needle is empty return 0
'''

def index_of(haystack, needle):
    i = 0
    needle_length = len(needle)
    if needle_length == 0:
        return 0
    limit = len(haystack) - needle_length
    idx = -1

    while i <= limit:
        j = 0
        no_match = False
        for x in range(i, i + needle_length, 1):
            if haystack[x] != needle[j]:
                no_match = True
                break
            j += 1
        if no_match is False:
            idx = i
            break
        i += 1
    
    return idx

haystack,needle = str(input('Enter haystack and needle(separated by comma) = ')).split(',')
print('Index of {} in {} is {}'.format(needle, haystack, index_of(haystack, needle)))