'''
    Return the index of the last occurrence of needle in haystack, or -1 if needle is not part of haystack.

    when needle is empty return 0
'''

def last_index_of(haystack, needle):
    i = 0
    needle_length = len(needle)
    if needle_length == 0:
        return 0
    idx = -1
    limit = len(haystack) - needle_length

    while i <= limit:
        j = 0
        match_found = True
        for x in range(i, i + needle_length, 1):
            if haystack[x] != needle[j]:
                match_found = False
                break
            j += 1
        if match_found:
            idx = i
        i += 1
    
    return idx

haystack,needle = str(input('Enter haystack and needle : ')).split(',')
print('Last index of {} in {} is {}'.format(needle, haystack, last_index_of(haystack, needle)))