
'''
    https://leetcode.com/problems/roman-to-integer/

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

    Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
'''

from timeit import default_timer as timer
import operator

ops = {
    '+': operator.add,
    '-': operator.sub
}

translate = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def roman_to_integer(roman):
    i = len(roman) - 1
    operator = ops['+']
    stack = 0
    handledPrev = False

    while i >= 0:
        if handledPrev is False:
            current = roman[i]
            if (i - 1) >= 0:
                prev = roman[i - 1]
            else:
                prev = None

            if (prev == 'I' and current in ['V', 'X']) or (prev == 'X' and current in ['L', 'C']) or (prev == 'C' and current in ['D', 'M']):
                current = ops['-'](translate[current], translate[prev])
                handledPrev = True

            if current in translate:
                current = translate[current]
            stack = operator(current, stack)
        else:
            handledPrev = False

        i -= 1

    return stack

roman = str(input('Enter roman number :: ')).upper()
start = timer()
integer = roman_to_integer(roman)
end = timer()
print('Integer form of roman number {} is {}'.format(roman, integer))
print('Time taken is {}'.format(end - start))

