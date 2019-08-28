from timeit import default_timer as timer

def calculate_exponent(number, exponent):
    answer = 0
    if exponent == 0:
        return 1
    elif exponent == 1:
        return 1
    else:
        answer = number << (exponent - 1)

    return answer

if __name__ == '__main__':
    test_cases = int(input('Enter number of test_cases :: '))
    for t in range(test_cases):
        number = int(input('Enter exponent :: '))
        start = timer()
        exp = str(calculate_exponent(2, number))
        sum = 0
        i = 0
        length = len(exp)
        while i < length:
            sum += int(exp[i])
            i += 1
        print('Sum of digits in 2 raised to power {} is {}'.format(number, sum))
        end = timer()
        print('Time taken is {}'.format(end - start))
