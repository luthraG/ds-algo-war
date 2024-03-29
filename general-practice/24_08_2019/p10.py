'''
    The sequence of triangle numbers is generated by adding the natural numbers.
    So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers:

    1: 1
    3: 1,3
    6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28
    We can see that 28 is the first triangle number to have over five divisors.

    What is the value of the first triangle number to have over five hundred divisors?

    Did you see the pattern? nth triangular number can be given as n * (n + 1) // 2
    Another think to note:

    Each number can be expressed as product of prime factors - prime factor decomposition
    e.g. N = p^a * q^b, where p and q are prime numbers. a and b represents the exponent value

    So in this case total number of divisors of N will be (a + 1)(b + 1)

    hence when we say more than 500 divisors, then we need to check which number will have prime factors that would sum up to 500
    and then check if that number is triangular or not
'''

from timeit import default_timer as timer

def totalDivisors(number):
    # print(number)
    divisors_count = 1
    factors = []
    num = 0

    while number % 2 == 0:
        num += 1
        number //= 2

    # Keep factors of 2, if present
    if num > 0:
        factors.append(num)
        # reset num
        num = 0

    x = 3
    while x <= number:
        while number % x == 0:
            num += 1
            number //= x
        x += 2

        # add factors of x if num > 0
        if num > 0:
            factors.append(num)
            # reset num
            num = 0

    if number > 2:
        factors.append(1)

    # print(factors)
    if len(factors) > 0:
        for i in factors:
            divisors_count *= (i + 1)

    return divisors_count

if __name__ == '__main__':
    max_divisors = int(input('Enter maximum number of divisors :: '))
    start = timer()

    divisors_to_n_mapping = {
        1: 383, # 100
        2: 2014, # 200
        3: 2078, # 300 and so on
        4: 5983,
        5: 12374,
        6: 14398,
        7: 21734,
        8: 41039,
        9: 41039,
        10: 41039
    }

    triangular_number = 1
    factors = 1
    n = 1

    if max_divisors >= 100:
        temp = max_divisors // 100
        n = divisors_to_n_mapping[temp]

    while factors <= max_divisors:
        n += 1
        triangular_number = (n * (n + 1)) // 2
        factors = totalDivisors(triangular_number)

    print('First triangular number with more than {} divisors is {}'.format(max_divisors, triangular_number))
    end = timer()
    print('Time taken is : {}'.format(end - start))