from timeit import default_timer as timer

def allRotations(number):
    length = len(number)
    i = 0
    rotations = []
    while i < length - 1:
        number = number[1:] + number[0]
        rotations.append(number)
        i += 1
    
    return rotations

def precalculatePrimes(number):
    primes = [True] * number
    sieve = {}
    sieve["2"] = True
    
    i = 3
    limit = int(number ** 0.5) + 1

    while i <= limit:
        if primes[i]:
            primes[i*i::2*i] = [False]*((number - i*i - 1)//(2*i) + 1)
        i += 2

    i = 3
    while i < number:
        if primes[i]:
            sieve[str(i)] = True
        i += 2

    return sieve

if __name__ == '__main__':
    number = int(input('Enter the number :: '))
    start = timer()
    max_number = 1000000
    sieve = precalculatePrimes(max_number)
    i = 2
    sum = 0
    while i < number:
        num = str(i)
        if num in sieve:
            circularPrime = True
            rotations = allRotations(num)
            for rot in rotations:
                if rot not in sieve or int(rot) > number:
                    circularPrime = False
                    break
            if circularPrime:
                sum += int(i)
        i += 1

    print('Sum of circular primes below {} is {}'.format(number, sum))

    end = timer()
    print('Time taken is {}'.format(end - start))