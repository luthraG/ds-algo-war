from timeit import default_timer as timer


def calculateFactorial(number):
    if number <= 1:
        return 1
    else:
        return number * calculateFactorial(number - 1)

if __name__ == '__main__':
    number = int(input("Enter a number :: "))
    start = timer()
    fac = calculateFactorial(number)
    end = timer()
    print("Factorial of {} is {}".format(number, fac))
    print("Time taken is {}".format(end - start))
