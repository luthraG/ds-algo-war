from timeit import default_timer as timer

if __name__ == '__main__':
    test_cases = int(input('Enter test cases :: '))
    for t in range(test_cases):
        number = int(input('Enter number :: '))
        start = timer()
        # since we need multiples below
        number -= 1
        mux3 = number // 3
        mux5 = number // 5
        mux15 = number // 15

        mux3 = 3 * ((mux3 * (mux3 + 1)) // 2)
        mux5 = 5 * ((mux5 * (mux5 + 1)) // 2)
        mux15 = 15 * ((mux15 * (mux15 + 1)) // 2)

        sum = mux3 + mux5 - mux15

        print('Sum of multiples of 3 and 5 below {} is {}'.format(number + 1, sum))
        end = timer()
        print('Time taken is {}'.format(end - start))
