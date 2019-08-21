'''

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

'''

from timeit import default_timer as timer

if __name__ == '__main__':
    number = int(input('Enter the number :: '))
    start = timer()

    sum = 0
    number -= 1 # Since we need below number i.e. number is not inclusive
    mulx3 = number // 3
    mulx5 = number // 5
    mulx15 = number // 15
    
    sum = (3 * mulx3 * (mulx3 + 1) // 2) + (5 * mulx5 * (mulx5 + 1) // 2) - (15 * mulx15 * (mulx15 + 1) // 2)
    print('Sum of multiples of 3 and 5 below {} is {}'.format(number + 1, sum))
    end = timer()
    print('Time taken is : {}'.format(end - start))