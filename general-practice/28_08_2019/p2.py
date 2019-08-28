from timeit import default_timer as timer

def largestPrimeFactor(number):
    largestFactor = -1

    while number % 2 == 0:
        largestFactor = 2
        number = number >> 1
    
    # Now take out odd factors as all even factors are taken out
    x = 3
    limit = int(number ** 0.5) + 1
    while x < limit:
        while number % x == 0:
            if largestFactor < x:
                largestFactor = x
            number //= x
        x += 2
    
    if number > 2:
        if largestFactor < number:
            largestFactor = number
    
    return largestFactor


if __name__ == '__main__':
    test_cases = int(input('Enter test cases :: '))
    for t in range(test_cases):
        number = int(input('Enter the number :: '))
        start = timer()
        print('Largest prime factor of {} is {}'.format(number, largestPrimeFactor(number)))
        end = timer()
        print('Time taken is : {}'.format(end - start))