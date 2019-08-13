from timeit import default_timer as timer

if __name__ == '__main__':
    start = timer()
    number = 100
    sum_of_squares = 0
    square_of_sum = 0
    diff = 0

    square_of_sum = square_of_sum + (number * (number + 1)) // 2
    sum_of_squares = ((2 * number + 1) * (square_of_sum)) // 3
    square_of_sum = square_of_sum * square_of_sum
    diff = square_of_sum - sum_of_squares

    print("The difference between the sum of the squares of the first {} natural numbers and the square of the sum is : {}", number, diff)

    end = timer()
    print("Time taken is {}".format((end - start)))
