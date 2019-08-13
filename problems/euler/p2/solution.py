from timeit import default_timer as timer


def additionFabonacii(limit):
    sequence = [1, 2]
    term = 0
    addition = 0
    if limit > 0:
        addition = addition + 2
    while term < limit:
        length = len(sequence)
        term = sequence[length - 1] + sequence[length - 2]
        if term < limit:
            if term % 2 == 0:
                addition = addition + term
            sequence.append(term)
    return addition

if __name__ == '__main__':
    limit = 10**16
    addition = 0
    start = timer()
    addition = additionFabonacii(limit)
    end = timer()
    print("Addition of even valued terms in Fabonacii series upto {} is {}".format(limit, addition))
    print("Time taken is {}".format(end - start))
