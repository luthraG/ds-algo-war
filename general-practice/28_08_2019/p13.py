from timeit import default_timer as timer

def factorial(number):
    if number <= 1:
        return 1
    else:
        previous_factor = 0
        is_odd = False

        if number & 1 != 0:
            is_odd = True
            number -= 1
        
        limit = number // 2
        i = 0
        fact = 1
        while i < limit:
            previous_factor = previous_factor + (number - (2 * i))
            fact *= previous_factor
            i += 1

        if is_odd:
            fact *= (number + 1)
        
        return fact


if __name__ == '__main__':
    test_cases = int(input('Enter the number of test_cases :: '))
    for t in range(test_cases):
        number = int(input('Enter the number :: '))
        start = timer()
        fact = str(factorial(number))
        i = 0
        sum = 0
        length = len(fact)
        while i < length:
            sum += int(fact[i])
            i += 1
        print('Sum of digits in factorial of {} is {}'.format(number, sum))
        end = timer()
        print('Time taken is {}'.format(end - start))
