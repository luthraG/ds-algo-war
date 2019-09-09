
def rwh_prime(number):
    primes = [True] * number
    sieve = []

    primes = [True] * (number // 2)
    limit = int(number ** 0.5) + 1

    for i in range(3, limit, 2):
        if primes[i//2]:
            primes[i*i//2::i] = [False]*((number - i*i - 1)//(2*i) + 1)
    
    for i in range(1, number // 2):
        if primes[i]:
            value = 2*i + 1
            if value not in [2, 3, 5, 7] and isPandigital(value):
                sieve.append(value)

    return sieve

def isPandigital(nr):
    # length = len(str(num))
    # arr = [0] * 10
    # pan = True
    # while num != 0:
    #     arr[num % 10] += 1
    #     num //= 10

    # i = 1
    # while i < 10:
    #     if i <= length:
    #         if arr[i] != 1:
    #             pan = False
    #             break
    #     else:
    #         if arr[i] != 0:
    #             pan = False
    #             break
    #     i += 1
    # return pan

    nr = str(nr)
    n = len(nr)
    beg=set(nr[0:n])
    end=set(nr[-n:])
    return beg==end and beg==set(map(str, range(1, n + 1)))

if __name__ == '__main__':
    sieve = rwh_prime(7654322)
    test_cases = int(input('Enter the number of test_cases :: '))
    for t in range(test_cases):
        number = int(input('Enter the number :: '))
        i = 0
        largest = -1

        if number >= 7652413:
            largest = 7652413
        else:
            i = 0
            prime = sieve[i]
            length = len(sieve)
            while prime <= number and i < length - 1:
                largest = prime
                i += 1
                prime = sieve[i]

        print(largest)

        
