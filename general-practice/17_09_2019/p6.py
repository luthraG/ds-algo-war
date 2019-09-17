'''
    The count-and-say sequence is the sequence of integers with the first five terms as following:

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221

    Given n, find the nth term
'''

def count_and_say_term(n):
    expression = '1'
    if n == 1:
        return expression
    else:
        term = 1
        while term != n:
            length = len(expression)
            i = 0
            count = 0
            stack = ''
            prev = None
            while i < length:
                item = expression[i]
                if prev is None:
                    count += 1
                    prev = item
                elif prev == item:
                    count += 1
                elif prev != item:
                    # This is new item, we need to update the stack
                    stack += str(count) + str(prev)
                    # Also reset prev and reset count
                    prev = item
                    count = 1
                i += 1
            
            stack += str(count) + str(prev)
            # Update the expression and term count
            expression = stack
            term += 1

        return expression
    
term = int(input('Enter the term number required for count and say expression :: '))
print('{} term of count and say expression is {}'.format(term, count_and_say_term(term)))