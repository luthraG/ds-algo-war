from timeit import default_timer as timer
import math

if __name__ == '__main__':
    test_cases = int(input('Enter number of test_cases :: '))
    five_sqrt = 5**0.5
    one_by_five_sqrt = 1 / five_sqrt
    phi_plus = (1 + five_sqrt)/2


    for t in range(test_cases):
        number = int(input('Enter number of digits :: '))
        start = timer()
        length = ((number - 1) - math.log(one_by_five_sqrt, 10)) / math.log(phi_plus, 10)
        print('First fibonacci number with {} digits is {}'.format(number, int(length + 1)))
        end = timer()
        print('Time taken is {}'.format(end - start))
