'''
    Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.
    It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

    Words in the list of banned words are given in lowercase, and free of punctuation.
    Words in the paragraph are not case sensitive.  The answer is in lowercase.
'''

import re

words_freq = {

}

def most_common_word(paragraph, banned_words):
    paragraph = paragraph.lower()
    pattern = re.compile(r'[a-z]+')

    for word in re.findall(pattern, paragraph):
        if word not in banned_words:
            if word in words_freq:
                words_freq[word] += 1
            else:
                words_freq[word] = 1

    items = []
    for key, value in words_freq.items():
        items.append((key, value))
    
    items.sort(key = lambda x: x[1], reverse = True)

    return items[0][0]

paragraph = str(input('Enter string :: '))
banned_words = str(input('Enter comma separated banned words :: ')).split(',')
banned_words = list(map(str, banned_words))

print('Most common word in input paragraph is {}'.format(most_common_word(paragraph, banned_words)))