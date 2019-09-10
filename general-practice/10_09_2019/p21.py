'''
    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
'''

from timeit import default_timer as timer

def calculateFactorial(number):
    is_odd = False
    if number & 1 == 1:
        number -= 1
        is_odd = True
    
    previous_factor = 0
    i = 0
    fact = 1
    limit = number // 2

    while i < limit:
        previous_factor = previous_factor + number - 2*i
        fact *= previous_factor
        i += 1
    
    if is_odd:
        fact *= (number + 1)

    return fact

number = int(input('Enter the number for which digits sum of its factorial is required :: '))
start = timer()
sum = 0

fact = calculateFactorial(number)

while fact != 0:
    sum += (fact % 10)
    fact //= 10

end = timer()
print('Sum of digits of factorial of {} is {}'.format(number, sum))
print('Time taken is {}'.format(end - start))