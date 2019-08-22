# coding: utf-8
'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms.

By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
'''

from timeit import default_timer as timer

if __name__ == '__main__':
    number = int(input('Enter upper limit for value of Fibonacci :: '))
    start = timer()
    sequence = [1, 2]
    sum = 2
    term = 0
    while term <= number:
        term = sequence[0] + sequence[1]
        sequence[0] = sequence[1]
        sequence[1] = term
        if term & 1 == 0 and term <= number:
            sum += term

    print('Sum of even valued terms of fibonacci series below {} is {}'.format(number, sum))
    end = timer()
    print('Time taken is : {}'.format(end - start))
