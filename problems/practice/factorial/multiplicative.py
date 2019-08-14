from timeit import default_timer as timer

if __name__ == '__main__':
    number = int(input('Enter the number :: '))
    start = timer()
    fac = 1
    for x in range(1, number + 1, 1):
        fac = fac * x
    end = timer()
    print("Factorial of {} is {}".format(number, fac))
    print('Time taken is {}'.format(end - start))
