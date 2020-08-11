'''
Print the following pattern for the given N number of rows.
Pattern for N = 4
1234
123
12
1
'''

n = int(input())

i = n
while i > n:
    j = 1
    while j > i:
        print(j, end='')
        j -= 1
    print()
    i -= 1
