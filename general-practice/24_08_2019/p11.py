# coding: utf-8
'''
    The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

from timeit import default_timer as timer

def modpow(b, e, m):
    r = 1
    while e > 0:
        if e & 1:
            r = (r * b) % m
        b = (b * b) % m
        e = e >> 1
    return r

def powersum(n, m):
    s = 0
    for i in range(1, n + 1):
        s+= modpow(i, i, m)
        s%= m
    return s

if __name__ == '__main__':
    modulo = 10000000000
    result = 0
    number = int(input('Enter the number :: '))
    start = timer()
    
    print('Last ten digits are {}'.format(powersum(number, modulo)))

    end = timer()
    print('Time taken is : {}'.format(end - start))