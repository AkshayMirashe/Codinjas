'''
Number Pattern
Print the following pattern for n number of rows.
For eg. N = 5

1        1
12      21
123    321
1234  4321
1234554321
'''

n = int(input())

i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end='')
        j += 1
    spaces = 1
    while spaces <= (2*n) - (i*2):
        print(' ', end='')
        spaces += 1
    a = 1
    b = i
    while a <= i:
        print(b, end='')
        a += 1
        b -= 1
    print()
    i += 1
