# coding: utf-8
'''
    Find the greatest product of K consecutive digits in the N digit number.

    Input Format

    First line contains T that denotes the number of test cases. 
    First line of each test case will contain two integers N & K. 
    Second line of each test case will contain a N digit integer.

    Constraints

    1 <= T <= 100
    1 <= K <= 7
    K <= N <= 1000

    Output Format

    Print the required answer for each test case.
'''

if __name__ == '__main__':
    test_cases = int(input().strip())
    for test_case in range(test_cases):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        number = input().strip()

        i = 0
        limit = n - k
        highest_product = 0

        div = 0
        previous_product = 0

        while i <= limit:
            product = 1
            if div == 0:
                for j in range(i, i + k, 1):
                    product *= int(number[j])
            else:
                product = (previous_product // div) * int(number[i + k - 1])
            
            # Set div and previous_product
            previous_product = product
            div = int(number[i])

            # Check if highest_product needs to be updated
            if product > highest_product:
                highest_product = product
            
            # Update loop counter to move to next k digits
            i += 1

        # Print the number which is highest multiple
        print(highest_product)

