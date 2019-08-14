from timeit import default_timer as timer


def calculateDigits(number):
    digits = 0
    while number != 0:
        digits += 1  # added for unit place
        number //= 10
    return digits

if __name__ == '__main__':
    number = int(input('Enter the number for number of digits in Fibonacci :: '))
    start = timer()
    sequence = [1, 1]
    term = 0
    digits = 0
    pos = 2
    while digits != number:
        term = sequence[0] + sequence[1]
        sequence[0] = sequence[1]
        sequence[1] = term
        pos += 1
        digits = calculateDigits(term)

    end = timer()
    print('First term that contains {} digits is {}'.format(number, pos))
    print('Time taken is {}'.format(end - start))
