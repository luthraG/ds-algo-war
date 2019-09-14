'''
    The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
'''

def count_and_say(n):
    if n <= 1:
        return '1'
    else:
        current_term = 1
        current_term_value = '1'
        while current_term != n:
            i = 0
            length = len(current_term_value)
            count = 1
            result = ''
            prev_item = None
            while i < length:
                item = current_term_value[i]
                if item == prev_item:
                    count += 1
                else:
                    if prev_item is not None:
                        result += str(count) + str(prev_item)
                        count = 1 # reset count
                    prev_item = item
                i += 1
            result += str(count) + str(prev_item)
            current_term_value = result
            current_term += 1
        return current_term_value

term = int(input('Enter term of count and say sequence :: '))
print('Value of {} term of sequence is {}'.format(term, count_and_say(term)))