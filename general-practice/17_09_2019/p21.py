'''
    Given a string text, you want to use the characters of text to form
    as many instances of the word "balloon" as possible.

    You can use each character in text at most once. Return the maximum number of instances that can be formed.

    Example 1:

    Input: text = "nlaebolko"
    Output: 1

    Example 2:

    Input: text = "loonbalxballpoon"
    Output: 2
    
    Example 3:

    Input: text = "leetcode"
    Output: 0
    

    Constraints:

    1 <= text.length <= 10^4
    text consists of lower case English letters only.
'''

def max_occurence_baloon(text):
    letters = [0] * 5 # Keep b a l o n
    i = 0
    length = len(text)

    while i < length:
        char = text[i]
        if char in 'ballon':
            if char == 'b':
                letters[0] += 1
            elif char == 'a':
                letters[1] += 1
            elif char == 'l':
                letters[2] += 1
            elif char == 'o':
                letters[3] += 1
            elif char == 'n':
                letters[4] += 1
        i += 1
    
    count = length
    for x in range(0,5,1):
        current = letters[x]
        if x == 2 or x == 3:
            current //= 2
        if current < count:
            count = current

    return count

text = str(input('Enter text = '))
print('Maximum occuences of baloon that can be formed from text are {}'.format(max_occurence_baloon(text)))