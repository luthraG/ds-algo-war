'''
    Roman to Integer

    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000
'''

from timeit import default_timer as timer

roman_to_integer_map = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def roman_string_to_integer(roman):
    i = len(roman) - 1
    stack = 0
    handledPrev = False

    while i >= 0:
        if handledPrev is False:
            current = roman[i]
            if i > 0:
                prev = roman[i - 1]
            else:
                prev = None
            
            if (prev == 'I' and current in ['V', 'X']) or (prev == 'X' and current in ['L', 'C']) or (prev == 'C' and current in ['D', 'M']):
                current = roman_to_integer_map[current] - roman_to_integer_map[prev]
                handledPrev = True
            
            if current in roman_to_integer_map:
                stack += roman_to_integer_map[current]
            else:
                stack += current
        else:
            handledPrev = False
        i -= 1

    return stack

input_string = str(input('Enter number in roman format :: '))

start = timer()
integer = roman_string_to_integer(input_string)
end = timer()

print('Integer form of roman number {} is {}'.format(input_string, integer))
print('Time taken is {}'.format(end - start))