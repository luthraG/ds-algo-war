from timeit import default_timer as timer

def sumOfPrimes(number):
    number += 1  # Since we want primes equal to number
    primes = [True] * number
    sum = [0] * number

    i = 3
    limit = int(number ** 0.5) + 1
    while i <= limit:
        if primes[i]:
            primes[i*i::2*i] = [False] * (((number - i*i - 1)//(2*i)) + 1)
        i += 2
    
    i = 3
    sum[2] = 2
    prev_sum = 2
    while i < number:
        if primes[i]:
            prev_sum += i
        sum[i] = prev_sum
        sum[i+1] = prev_sum
        i += 2

    return sum
if __name__ == '__main__':
    test_cases = int(input('Enter the test cases :: '))
    for t in range(test_cases):
        number = int(input('Enter the number :: '))
        start = timer()
        max_limit = 1000000
        sum = sumOfPrimes(max_limit)
        print('Sum of primes not greater than {} is {}'.format(number, sum[number]))
        end = timer()
        print('Time taken is : {}'.format(end - start))
    