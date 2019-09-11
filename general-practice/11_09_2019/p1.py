'''
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
'''

from timeit import default_timer as timer

upper_limit = int(input('Enter upper limit of number :: '))

start = timer()
upper_limit -= 1 # Since we need below this number

mux_3 = upper_limit // 3
mux_5 = upper_limit // 5
mux_15 = upper_limit // 15

sum_3 = 3 * ((mux_3 * (mux_3 + 1)) // 2)
sum_5 = 5 * ((mux_5 * (mux_5 + 1)) // 2)
sum_15 = 15 * ((mux_15 * (mux_15 + 1)) // 2)

overall_sum = sum_3 + sum_5 - sum_15

end = timer()
print('Sum of all multiples of 3 and 5 below {} is {}'.format((upper_limit + 1), overall_sum))
print('Time taken is {}'.format(end - start))
