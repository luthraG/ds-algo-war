from timeit import default_timer as timer

if __name__ == '__main__':
    mod = 1000000007
    test_cases = int(input('Enter the test cases :: '))
    for t in range(test_cases):
        number = int(input('Enter the number :: '))
        start = timer()
        number = (number - 1) // 2
        temp = (8 * number * number) + (15 * number) + 13
        sum = 1 + ((2 * number * temp) // 3)
        sum = sum % mod
        end = timer()
        print('Time taken is {}'.format(end - start))
        print(sum)
