'''
Print the following pattern for the given N number of rows.
Pattern for N = 4
1
11
121
1221
'''

n = int(input())

i = 1
if n != 0:
    while i <= n:
        j = 1
        while j <= i:
            if i <= 2:
                print('1', end='')
            elif j == 1 or j == i:
                print('1', end='')
            else:
                print('2', end='')
            j += 1
        print()
        i += 1
