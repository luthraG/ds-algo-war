'''
    Given an arbitrary ransom note string and another string containing letters from all the magazines,
    write a function that will return true if the ransom note can be constructed from the magazines ;
    otherwise, it will return false.

    Each letter in the magazine string can only be used once in your ransom note.

    Note:
    You may assume that both strings contain only lowercase letters.

    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false
    canConstruct("aa", "aab") -> true

'''

def can_construct_ransom_note(ransom, magazine):
    letters = [0] * 26
    START_INDEX = 97

    length1 = len(ransom)
    length2 = len(magazine)

    if length1 > length2:
        return False
    else:
        i = 0
        while i < length2:
            idx = ord(magazine[i]) - START_INDEX
            letters[idx] += 1
            i += 1

        i = 0
        while i < length1:
            idx = ord(ransom[i]) - START_INDEX
            letters[idx] -= 1
            if letters[idx] < 0:
                return False
            i += 1

        i = 0
        while i < 26:
            if letters[i] < 0:
                return False
            i += 1
        return True

ransom,magazine = str(input('Enter ransom note and magazine(separated by comma) = ')).split(',')
ransom,magazine = str(ransom),str(magazine)

print('Ransom can be constructed from magazine letters {}'.format(can_construct_ransom_note(ransom, magazine)))