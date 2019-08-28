from timeit import default_timer as timer

if __name__ == '__main__':
    test_cases = int(input('Enter the number of test cases :: '))
    for t in range(test_cases):
        number = int(input('Enter the number :: '))
        start = timer()
        sumOfNumbers = (number * (number + 1)) // 2
        sumOfSquares = (sumOfNumbers * (2*number + 1)) // 3
        diff = sumOfNumbers * sumOfNumbers - sumOfSquares
        print('Difference between square of sum of number and sum of squares up to {} is {}'.format(number, diff))
        end = timer()
        print('Time taken is {}'.format(end - start))