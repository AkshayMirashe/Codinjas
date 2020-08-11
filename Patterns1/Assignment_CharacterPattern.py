'''
Print the following pattern for the given N number of rows.
Pattern for N = 4
A
BC
CDE
DEFG
'''
n = int(input())

i = 1
while i <= n:
    j = 1
    k = i
    while j <= i:
        char = ord('A') + k - 1
        alpha = chr(char)
        print(alpha, end='')
        k += 1
        j += 1
    print()
    i += 1
