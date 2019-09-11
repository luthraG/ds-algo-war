class Anagram:
    def is_anagram(self, str1, str2):
        anagram = True
        length1 = len(str1)
        length2 = len(str2)

        if length1 != length2:
            anagram = False
        else:
            START_INDEX = 97
            items = [0] * 26

            i = 0
            while i < length1:
                idx1 = ord(str1[i]) - START_INDEX
                idx2 = ord(str2[i]) - START_INDEX
                items[idx1] += 1
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
    anagram = Anagram()
    str1 = str(input('Enter first string for anagram check :: '))
    str2 = str(input('Enter second string for anagram check :: '))
    print('Input strings are anagram :: {}'.format(anagram.is_anagram(str1, str2)))
