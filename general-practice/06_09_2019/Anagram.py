# As per google, an anagram is :: 
# a word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp.

START_INDEX = 97

str1 = input('Enter first string :: ').lower()
str2 = input('Enter second string :: ').lower()

# As we have 26 alphabets
anagram_chars = [0]*26
is_anagram = True

if len(str1) != len(str2):
    print('Not Anagram')
else:
    for c in str1.strip():
        idx = ord(c) - START_INDEX
        anagram_chars[idx] += 1
    
    for c in str2.strip():
        idx = ord(c) - START_INDEX
        anagram_chars[idx] -= 1

    for i in range(0, 26, 1):
        if anagram_chars[i] != 0:
            is_anagram = False
            break
    
    if is_anagram:
        print('Anagram')
    else:
        print('Not Anagram')
