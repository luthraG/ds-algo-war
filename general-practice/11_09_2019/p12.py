'''
    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
'''

from timeit import default_timer as timer

def calculate_factorial(number):
    is_odd = False

    if number & 1 == 1:
        number -= 1
        is_odd = True
    
    prod = 1
    previous_factor = 0
    limit = number // 2
    i = 0
    while i < limit:
        previous_factor = previous_factor + (number - 2 * i)
        prod *= previous_factor
        i += 1
    
    if is_odd:
        prod *= (number + 1)
    
    return prod

number = int(input('Calculate the number for which sum of digits of its factorial required :: '))
start = timer()
fact = calculate_factorial(number)
sum_of_digits = 0
fact = str(fact)
length = len(fact)
i = 0
while i < length:
    sum_of_digits += int(fact[i])
    i += 1

end = timer()
print('Sum of digits of factorial of {} is {}'.format(number, sum_of_digits))
print('Time taken is {}'.format(end - start))
