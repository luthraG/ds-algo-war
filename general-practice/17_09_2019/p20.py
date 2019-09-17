'''
    Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.
    It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

    Words in the list of banned words are given in lowercase, and free of punctuation. 
    Words in the paragraph are not case sensitive.  The answer is in lowercase.


Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
'''

import re

def most_frequent_words(paragraph, banned_words):
    paragraph = paragraph.lower()
    pattern = re.compile(r'[a-zA-Z0-9]+')
    highest_count = 0
    highest_count_word = ''
    words_freq = {

    }
    for word in re.findall(pattern, paragraph):
        if word not in banned_words:
            if word in words_freq:
                words_freq[word] += 1
            else:
                words_freq[word] = 1
    
    for key, value in words_freq.items():
        if value > highest_count:
            highest_count = value
            highest_count_word = key
    
    return highest_count_word


paragraph = str(input('Enter paragraph = '))
banned_words = str(input('Enter list of banned words(separated by comma) = ')).split(',')
banned_words = list(map(str, banned_words))
print('Most frequent word is {}'.format(most_frequent_words(paragraph, banned_words)))