'''
Print the following pattern for the given N number of rows.
Pattern for N = 4
1
11
202
3003
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
                print(i - 1, end='')
            else:
                print('0', end='')
            j += 1
        print()
        i += 1
# else:
#     print(1)
