from timeit import default_timer as timer

if __name__ == '__main__':
    number = int(input("Enter the number :: "))
    start = timer()
    addition = 0

    number = number - 1
    mux1 = number // 3
    mux2 = number // 5
    mux3 = number // 15

    addition = addition + 3 * ((mux1 * (mux1 + 1)) // 2)
    addition = addition + 5 * ((mux2 * (mux2 + 1)) // 2)
    addition = addition - 15 * ((mux3 * (mux3 + 1)) // 2)
    end = timer()
    print("Sum of multiples of 3 and 5 below {} is {}".format(number + 1, addition))
    print("Time taken is {}".format(end - start))
