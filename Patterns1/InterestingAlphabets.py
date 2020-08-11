'''
Print the following pattern for the given number of rows.
Pattern for N = 5
E
DE
CDE
BCDE
ABCDE
'''

n = int(input())

i = 1
while i <= n:
    j = 1
    while j <= i:
        alpha = chr((64 + n) + j - i)
        print(alpha, end='')
        j += 1
    print()
    i += 1
