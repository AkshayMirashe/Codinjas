'''
Print the following pattern for the given N number of rows.
Pattern for N = 3
 A
 BB
 CCC
 '''

n = int(input())

i = 1
while i <= n:
    j = 1
    while j <= i:
        alpha = chr(64 + i)
        print(alpha, end='')
        j += 1
    print()
    i += 1
