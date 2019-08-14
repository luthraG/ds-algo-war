from timeit import default_timer as timer

if __name__ == '__main__':
    number = int(input("Enter the upper limit of number :: "))
    start = timer()
    addition = 0
    sequence = [1, 2]
    term = 0

    if number <= 1:
        sequence = []

    # Let us add value of 2
    addition = addition + 2

    while term <= number and len(sequence) == 2:
        term = sequence[0] + sequence[1]
        if term <= number:
            sequence[0] = sequence[1]
            sequence[1] = term
            if term % 2 == 0:
                addition = addition + term

    end = timer()
    print("Sum of even valued terms for Fibonacii series below {} is {}".format(number, addition))
    print("Time taken is {}".format(end - start))
