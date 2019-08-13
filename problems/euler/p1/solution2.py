from timeit import default_timer as timer

if __name__ == '__main__':
    start = timer()
    number = 1000000000
    addition = 0
    number = number - 1
    mux1 = int(number // 3)
    mux2 = int(number // 5)
    mux3 = int(number // 15)
    addition = addition + (3 * ((mux1 * (mux1 + 1)) // 2))
    addition = addition + (5 * ((mux2 * (mux2 + 1)) // 2))
    addition = addition - (15 * ((mux3 * (mux3 + 1)) // 2))
    end = timer()
    print("Addition is = {}".format(addition))
    print("Time taken is {}".format(end - start))
