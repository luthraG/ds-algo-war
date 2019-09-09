def triangular(num):
    is_triangular = False
    temp = (-1 + ((1 + 8 * num) ** 0.5))
    if temp % 2 == 0:
        is_triangular = True
    
    return is_triangular, int(temp // 2)

if __name__ == '__main__':
    test_cases = int(input('Enter the number of test_cases :: '))
    for t in range(test_cases):
        number = int(input('Enter the number :: '))
        is_triangular, n = triangular(number)
        if is_triangular:
            print(n)
        else:
            print(-1)