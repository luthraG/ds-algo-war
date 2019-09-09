from timeit import default_timer as timer

def rwh_prime(number):
    primes = [True] * number
    sieve = {}
    sieve[1] = 2

    primes = [True] * (number // 2)
    limit = int(number ** 0.5) + 1

    for i in range(3, limit, 2):
        if primes[i//2]:
            primes[i*i//2::i] = [False]*((number - i*i - 1)//(2*i) + 1)
    
    counter = 1
    for i in range(1, number // 2):
        if primes[i]:
            counter += 1
            value = 2*i + 1
            sieve[counter] = value

    return sieve

if __name__ == '__main__':
    # start = timer()
    sieve = rwh_prime(2620000)
    length = len(sieve)
    test_cases = int(input('Enter the number of test_cases :: '))
    # test_cases = 5
    for t in range(test_cases):
        remainder_limit = int(input('Enter the remainder upper limit :: '))
        # remainder_limit = 1000000000000
        n = 1

        prime = sieve[n]
        remainder = 0

        if remainder_limit == 0 or remainder_limit == 1:
            n = 2
        else:
            n = length - 1
            if n & 1 == 0:
                n -= 1
            remainder = sieve[n] * n * 2
            while remainder > remainder_limit:
                n //= 2
                if n & 1 == 0:
                    n -= 1
                remainder = sieve[n] * n * 2

            while remainder < remainder_limit and n + 2 < length:
                n += 2
                prime = sieve[n]
                remainder = 2 * prime * n
        
        print(n)
    # end = timer()
    # print('Time taken is {}'.format(end - start))
