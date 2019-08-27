'''
    The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13
    This is the longest sum of consecutive primes that adds to a prime below one-hundred.

    The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

    Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

from timeit import default_timer as timer

def precalculateSieve(number):
    # number += 1
    sieve = [True] * number
    primesTable = {}
    primes = []

    sieve[0] = False
    sieve[1] = False

    x = 3
    limit = int(number ** 0.5) + 1
    while x <= limit:
        if sieve[x] == True:
            sieve[x*x::2*x] = [False] * ((number - x*x - 1)//(2*x) + 1)
        x += 2
    
    x = 3
    primesTable[2] = True
    primes.append(2)
    while x < number:
        if sieve[x]:
            primesTable[x] = True
            primes.append(x)
        x += 2

    return primesTable, primes

if __name__ == '__main__':
    number = int(input('Enter the number : '))
    start = timer()
    primesTable, primes = precalculateSieve(number)

    length = len(primes)
    i = 0
    maxSum = 0
    longestSeq = -1
    while i < length:
        sum = 0
        seq = 0
        j = i
        while j < length:
            if sum > number:
                break
            sum += primes[j]
            seq += 1
            if sum in primesTable and sum > maxSum and seq > longestSeq:
                maxSum = sum
                longestSeq = seq
            j += 1
        i += 1
    
    print('Prime number with longest sequence of primes that adds to a prime below {} is {}'.format(number, maxSum))
    end = timer()
    print('Time taken is : {}'.format(end - start))