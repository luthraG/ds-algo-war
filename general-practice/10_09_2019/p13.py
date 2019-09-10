'''
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
'''

def largestPrimeFactors(number):
    if number <= 1:
        return 0
    factors = []

    while number % 2 == 0:
        factors.append(2)
        number //= 2
    
    i = 3
    limit = int(number ** 0.5) + 1
    for i in range(3, limit, 2):
        while number % i == 0:
            factors.append(i)
            number //= i
        
        if number == 0:
            break
    
    if number > 2:
        factors.append(number)

    return factors[-1]

number = int(input('Enter number for which largest prime factor is required :: '))
print('Largest prime factor of {} is {}'.format(number, largestPrimeFactors(number)))
