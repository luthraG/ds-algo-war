from timeit import default_timer as timer

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
    return (a * (b // gcd(a, b)))

if __name__ == '__main__':
    test_cases = int(input('Enter the test_cases :: '))
    for t in range(test_cases):
        number = int(input('Enter the number :: '))
        start = timer()
        x = 1
        leastMultiple = 1
        while x <= number:
            leastMultiple = lcm(x, leastMultiple)
            x += 1
        end = timer()
        print('least multiple of number from 1 to {} is {}'.format(number, leastMultiple))
        print('Time taken is : {}'.format(end - start))