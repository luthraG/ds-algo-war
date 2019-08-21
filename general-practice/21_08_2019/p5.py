'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. 
What is the smallest positive number that is evenly divisible(divisible with no remainder) by all of the numbers from 1 to N?

Input Format

First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N.

Constraints

1 <= T <= 10
1 <= N <= 40

Output Format

Print the required answer for each test case.
'''

def gcd(a, b):
    if a > b:
        num = a
        den = b
    else:
        num = b
        den = a
    
    rem = num % den

    while rem != 0:
        num = den
        den = rem
        rem = num % den

    return den

def lcm(a, b):
    return ((a // gcd(a, b)) * b)

if __name__ == '__main__':
    test_cases = int(input('Enter the test cases :: '))
    for n in range(test_cases):
        number = int(input('Enter the number :: '))
        leastMultiple = 1
        i = 1
        while i <= number:
            leastMultiple = lcm(i, leastMultiple)
            i += 1
        print(leastMultiple)
