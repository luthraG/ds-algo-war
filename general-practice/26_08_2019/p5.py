if __name__ == '__main__':
    mod = 1000000007
    test_cases = int(input())
    for test_case in range(test_cases):
        number = int(input())
        number = (number - 1) // 2
        temp = (8*number*number + 15*number + 13)
        sum = 1 + ((2 * number * temp) // 3)
        sum = sum % mod

        print(sum)
