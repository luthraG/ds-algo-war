'''
    https://leetcode.com/problems/reorder-data-in-log-files/


    You have an array of logs.  Each log is a space delimited string of words.

    For each log, the first word in each log is an alphanumeric identifier.  Then, either:

    1. Each word after the identifier will consist only of lowercase letters, or;
    2. Each word after the identifier will consist only of digits.
    
    We will call these two varieties of logs letter-logs and digit-logs.
    It is guaranteed that each log has at least one word after its identifier.

    Reorder the logs so that all of the letter-logs come before any digit-log.
    The letter-logs are ordered lexicographically ignoring identifier,
    with the identifier used in case of ties.
    
    The digit-logs should be put in their original order.

    Return the final order of the logs.

    Example 1:

    Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
    

    Constraints:

    0 <= logs.length <= 100
    3 <= logs[i].length <= 100
    logs[i] is guaranteed to have an identifier, and a word after the identifier.
'''

def order_logs(items):
    i = 0
    length = len(items)
    str_length = 0

    strings = []
    numbers = []

    while i < length:
        item = items[i]
        first_space = item.index(' ')
        if item[first_space + 1].isdigit():
            numbers.append(item)
        else:
            str_length += 1
            strings.append(item[first_space + 1:] + ' ' + item[0:first_space])
        i += 1

    items = []
    # Now we need to sort strings and then extend it by numbers
    strings.sort()

    i = 0
    while i < str_length:
        item = strings[i]
        splits = item.rsplit(' ', 1)
        item = splits[1] + ' ' + splits[0]
        strings[i] = item
        i += 1
    strings.extend(numbers)

    return strings


    
items = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
items = order_logs(items)
print(items)