'''
    https://leetcode.com/problems/roman-to-integer/

    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
'''

roman_to_integer_map = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def roman_to_integer(roman = ''):
    roman = roman.upper()
    i = len(roman) - 1
    handledPrev = False
    overall_sum = 0

    while i >=0:
        if handledPrev is False:
            current = roman[i]
            if i - 1 >= 0:
                prev = roman[i - 1]
            else:
                prev = None

            if (prev == 'I' and current in ['V', 'X']) or (prev == 'X' and current in ['L', 'C']) or ((prev == 'C') and current in ['D', 'M']):
                current = roman_to_integer_map[current] - roman_to_integer_map[prev]
                handledPrev = True
            
            overall_sum += current if current not in roman_to_integer_map else roman_to_integer_map[current]
        else:
            handledPrev = False
        
        i -= 1
    
    return overall_sum

roman = str(input('Enter roman number :: '))
integer = roman_to_integer(roman)
print('Integer number corresponding to roman number {} is {}'.format(roman, integer))
