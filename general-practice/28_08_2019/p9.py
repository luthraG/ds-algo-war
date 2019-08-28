from timeit import default_timer as timer

def total_divisors(triangular_number):
    divisors = 0
    total = 1
    while triangular_number % 2 == 0:
        divisors += 1
        triangular_number //= 2
    
    total *= (divisors + 1) # Helps in constant time fetch

    i = 3
    while i <= triangular_number:
        divisors = 0
        while triangular_number % i == 0:
            divisors += 1
            triangular_number //= i
        total *= (divisors + 1)
        i += 2

    divisors = 0
    if triangular_number > 2:
        divisors += 1
        total *= (divisors + 1)
    
    return total

if __name__ == '__main__':
    test_cases = int(input('Enter the number of test_cases :: '))
    divisors_to_n_mapping = {
        1: 384,
        2: 2015,
        3: 2079,
        4: 5984,
        5: 12375,
        6: 14399,
        7: 21735,
        8: 41040,
        9: 41040,
        10: 41040
    }
    for t in range(test_cases):
        max_divisors = int(input('Enter the maximum number of divisors :: '))
        start = timer()
        n = 1
        divisors = 0
        if max_divisors >= 100:
            n = divisors_to_n_mapping[max_divisors // 100]
        while divisors <= max_divisors:
            triangular_number = (n * (n + 1)) // 2
            divisors = total_divisors(triangular_number)
            n += 1

        print('First triangular number to have more than {} divisors is {}'.format(max_divisors, triangular_number))
        end = timer()
        print('Time taken is {}'.format(end - start))
