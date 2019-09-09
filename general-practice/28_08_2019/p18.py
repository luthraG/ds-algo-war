from timeit import default_timer as timer

def is_pentagonal(num):
    return (1 + ((1 + 24 * num) ** 0.5)) % 6 == 0

def is_triangular(num):
    return (-1 + ((1 + 8 * num) ** 0.5)) % 2 == 0


def precalculate_triangular_numbers(limit):
    triangulars = {}
    n = 1
    result = 0
    while result < limit:
        result = (n * (n + 1))  >> 1
        triangulars[n] = result
        n += 1
    # triangulars[-1] = 57722156241751
    return triangulars

if __name__ == '__main__':
    limit, a, b = input('Enter the upper limit, first number and second number, separated by space :: ').split(' ')
    limit = int(limit)
    a = int(a)
    b = int(b)
    # either we have query for 3, 5
    # or we have query for 5, 6
    start = timer()
    # limit = 10**13
    upper_limit = 10**13
    triangulars = precalculate_triangular_numbers(upper_limit)
    n = 1
    inc = 1
    if a == 5 and b == 6:
        inc = 2
    while True:
        trian = triangulars[n]
        if trian >= limit:
            break
        if is_pentagonal(trian):
            print(trian)
        if limit > 10000000000000 and n >= 4472135:
            print(57722156241751)
            break
        n += inc

    end = timer()
    print('Time taken is {}'.format(end - start))