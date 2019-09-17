'''
    Let's define a function f(s) over a non-empty string s,
    which calculates the frequency of the smallest character in s.
    For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

    Now, given string arrays queries and words,
    return an integer array answer,
    where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.

Example 1:

Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").

Example 2:

Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]

Explanation: On the first query only f("bbb") < f("aaaa").
On the second query both f("aaa") and f("aaaa") are both > f("cc").
'''

letter_to_ascii_map = {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}

def frequency_of_smallest_char(word):
    letters = [0] * 26
    START_INDEX = 97

    i = 0
    length = len(word)

    while i < length:
        letters[letter_to_ascii_map[word[i]] - START_INDEX] += 1
        i += 1

    i = 0
    while i < 26:
        if letters[i] > 0:
            return letters[i]
        i += 1

    return 0

def solution_for_queries_words(queries, words):
    # word_frequencies = []
    answer = []
    # for word in words:
    #     word_frequencies.append(frequency_of_smallest_char(word))

    query_counts = [word.count(min(word)) for word in queries]
    word_counts = [word.count(min(word)) for word in words]
    
    for freq in query_counts:
        answer.append(sum(frequency > freq for frequency in word_counts))

    # for query in queries:
    #     freq = frequency_of_smallest_char(query)
    #     answer.append(sum(frequency > freq for frequency in word_frequencies))

    return answer

queries = str(input('Enter queries(comma separated) = ')).split(',')
words = str(input('Enter words(comma separated) = ')).split(',')

queries = list(map(str, queries))
words = list(map(str, words))

print('Answer is {}'.format(solution_for_queries_words(queries, words)))