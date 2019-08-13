from timeit import default_timer as timer


def calculatePower(base, power):
    if power < 0:
        return calculatePower(1 // base, -1 * power)
    if power == 0:
        return 1
    elif base == 0:
        return 0
    elif power == 1:
        return base
    elif (power & 1) != 0:
        return base * calculatePower(base * base, (power - 1) // 2)
    else:
        return calculatePower(base * base, power // 2)

if __name__ == '__main__':
    start = timer()
    power = 1000
    base = 2
    addition = 0

    output = calculatePower(base, power)
    output2 = output
    while output != 0:
        addition = addition + output % 10
        output = output // 10

    end = timer()
    print("{} raised to {} is {}".format(base, power, output2))
    print("Sum of digits of output is : {}".format(addition))
    print("Time taken is {}".format((end - start)))
