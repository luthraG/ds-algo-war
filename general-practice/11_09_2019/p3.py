'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from timeit import default_timer as timer

def largestPrimeFactor(number):
    if number == 1:
        return 0

    factors = []
    while number % 2 == 0:
        factors.append(2)
        number //= 2

    limit = int(number ** 0.5) + 1
    for i in range(3, limit, 2):
        while number % i == 0:
            factors.append(i)
            number //= i

    if number > 2:
        factors.append(number)
    
    return factors[-1]

number = int(input('Enter the number whose prime factor is required :: '))
start = timer()
largest_prime_factor = largestPrimeFactor(number)
end = timer()
print('Largest prime factor of {} is {}'.format(number, largest_prime_factor))
print('Time taken is {}'.format(end - start))