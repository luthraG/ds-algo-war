from timeit import default_timer as timer

if __name__ == '__main__':
    test_cases = int(input('Enter the test cases :: '))
    for t in range(test_cases):
        number = int(input('Enter the number :: '))
        start = timer()

        sequence = [1, 2]
        term = 0
        sum = 2
        while term <= number:
            term = sequence[0] + sequence[1]
            sequence[0] = sequence[1]
            sequence[1] = term
            if term <= number and term & 1 == 0:
                sum += term

        print('Sum of even valued fibonacci below {} is {}'.format(number, sum))
        end = timer()
        print('Time taken is : {}'.format(end - start))