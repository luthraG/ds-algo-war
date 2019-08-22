import math

def rwh_primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def rwh_primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::2*i//2]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [2*i + 1 for i in range(1,n//2) if sieve[i]]

if __name__ == '__main__':
    test_cases = int(input())
    for t in range(test_cases):
        number = int(input())
        if number <= 6:
            primes = [2, 3, 5, 7, 11, 13]
            print(primes[number - 1])
        else:
            n = int(number * (math.log(number) + math.log(math.log(number)))) + 3
            print(rwh_primes1(n)[number - 1])
