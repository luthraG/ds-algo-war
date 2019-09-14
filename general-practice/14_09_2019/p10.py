'''
    Given an arbitrary ransom note string and another string containing letters from all the magazines,
    write a function that will return true if the ransom note can be constructed from the magazines;
    otherwise, it will return false.

    Each letter in the magazine string can only be used once in your ransom note.

    Note:
    You may assume that both strings contain only lowercase letters.
'''

def can_ransom_note_constructed(magazine, ransom):
    START_INDEX = 97
    letters = [0] * 26

    length = len(magazine)
    length1 = len(ransom)

    if length1 > length:
        return False
    else:
        i = 0
        while i < length:
            letters[ord(magazine[i]) - START_INDEX] += 1
            i += 1
        
        i = 0
        while i < length1:
            letters[ord(ransom[i]) - START_INDEX] -= 1
            i += 1
        
        i = 0
        while i < 26:
            if letters[i] < 0:
                return False
            i += 1
    
        return True

magazine = str(input('Enter letters of magazine :: '))
ransom = str(input('Enter letters of ransom note :: '))

print('can ransom note be constructed from letters of magazine : {}'.format(can_ransom_note_constructed(magazine, ransom)))