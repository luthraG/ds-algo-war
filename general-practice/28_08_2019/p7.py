from timeit import default_timer as timer

if __name__ == '__main__':
    test_cases = int(input('Enter the number of test_cases :: '))
    for t in range(test_cases):
        number_digits, consecutive_digits = input('Enter the number of digits and space separated consecutive number of digits :: ').split(' ')
        number_digits, consecutive_digits = [int(number_digits), int(consecutive_digits)]
        number = str(input('Enter the number :: ')) # Reading number as integer is memory intensive
        start = timer()
        max_product = 0
        x = 0
        limit = number_digits - consecutive_digits
        while x < limit:
            product = 1
            for idx in range(x, x + consecutive_digits, 1):
                product *= int(number[idx])
            if product > max_product:
                max_product = product
            x += 1

        end = timer()
        print('Greatest product of {} consecutive digits in {} is {}'.format(consecutive_digits, number, max_product))
        print('Time taken is : {}'.format(end - start))
