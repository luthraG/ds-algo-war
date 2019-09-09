
if __name__ == '__main__':
    str1 = input('Enter first string = ').lower()
    str2 = input('Enter second string = ').lower()

    START_INDEX = 97
    i = 0
    is_anagram = True
    anagram = [0]*26

    chars1 = str1.strip()
    length1 = len(chars1)

    chars2 = str2.strip()
    length2 = len(chars2)

    if len(chars1) != len(chars2):
        print('Strings are not anagram')
    else:
        while i < length1:
            idx1 = ord(chars1[i]) - START_INDEX
            idx2 = ord(chars2[i]) - START_INDEX
            anagram[idx1] += 1
            anagram[idx2] -= 1
            i += 1
        
        i = 0
        while i < 26:
            if anagram[i] != 0:
                is_anagram = False
                break
            i += 1
        
        if is_anagram:
            print('Strings are anagram')
        else:
            print('Strings are not anagram')