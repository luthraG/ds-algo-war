def is_anagram(str1, str2):
    anagram = True

    if len(str1) != len(str2):
        return False
    else:
        str1 = str1.lower()
        str2 = str2.lower()

        # As there are 26 alphabets
        items = [0] * 26

        START_INDEX = 97

        i = 0
        length = len(str1)
        while i < length:
            idx = ord(str1[i]) - START_INDEX
            idx2 = ord(str2[i]) - START_INDEX
            items[idx] += 1
            items[idx2] -= 1
            i += 1

        i = 0
        while i < 26:
            if items[i] != 0:
                anagram = False
                break
            i += 1
        
        return anagram

if __name__ == '__main__':
    str1 = str(input('Enter first string :: '))
    str2 = str(input('Enter second string :: '))
    print('Strings are Anagram :: {}'.format(is_anagram(str1, str2)))

