'''
Write a code to return a value 'True' if the number '1' throughout the array appears consecutively.
Ex: S = {1,1,1,0,0,3,4}. 
Else, return 'False' if the array does not have the given number (char = '1' in this case) in the consecutive order.
Ex: S = {1,1,0,0,1,3,4}
'''

number = int(input('Enter number to check for consecutive occurences :: '))

items = [1,1,1,0,0,3,4]
# items = [1,1,0,0,1,3,4]
items = [1,1,1,0,0,3,4,1,1,1,3]

idx = 0
length = len(items)
prev_occ = -1
is_consecutive = True
while idx < length:
    if items[idx] == number:
        if prev_occ == -1:
            prev_occ = idx
        else:
            if idx == prev_occ + 1:
                prev_occ = idx
            else:
                is_consecutive = False
                break
    idx += 1

if is_consecutive:
    print('All occurences of {} are consecutive'.format(number))
else:
    print('All occurences of {} are NOT consecutive'.format(number))