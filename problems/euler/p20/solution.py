from timeit import default_timer as timer


def calculateFactorial(number):
    if number <= 1:
        return 1
    else:
        is_odd = False
        previous_factor = 0
        limit = number // 2
        fact = 1

        if number & 1 == 1:
            is_odd = True
            number = number - 1

        x = 0
        while x < limit:
            previous_factor = previous_factor + (number - 2 * x)
            fact *= previous_factor
            x += 1

        if is_odd:
            fact *= (number + 1)
        return fact


if __name__ == '__main__':
    number = int(input('Enter the number :: '))
    start = timer()
    fact = calculateFactorial(number)
    addition = 0
    while fact != 0:
        addition += (fact % 10)
        fact //= 10
    end = timer()
    print('Sum of digits for factorial of {} is {}'.format(number, addition))
    print('Time taken is {}'.format(end - start))
