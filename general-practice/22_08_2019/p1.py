'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

from timeit import default_timer as timer

if __name__ == '__main__':
    number = int(input('Enter upper range of number :: '))
    start = timer()
    sum = 0
    number -= 1
    n3 = number // 3
    n5 = number // 5
    n15 = number // 15

    sum += 3 * n3 * (n3 + 1) // 2
    sum += 5 * n5 * (n5 + 1) // 2
    sum -= 15 * n15 * (n15 + 1) // 2

    print('Sum of multiples of 3 and 5 below {} is {}'.format(number + 1, sum))

    end = timer()
    print('Time taken is : {}'.format(end - start))
