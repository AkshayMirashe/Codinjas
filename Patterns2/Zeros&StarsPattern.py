'''
Zeros and Stars Pattern
Print the following pattern
Pattern for N = 4

*000*000*
0*00*00*0
00*0*0*00
000***000
'''
# Solution divided in two halves
# *000*
# 0*00*
# 00*0*
# 000**

# and

# 000*
# 00*0
# 0*00
# *000


# STRATEGY ==> After j = 1, under a big while loop all if cases are fitted.

n = int(input())

a = (2 * n) + 1  # To print * in the second pattern
i = 1
while i <= n:
    j = 1
    while j <= (2 * n) + 1:  # To print columns till 2n+1
        if j <= n:
            if i == j:
                print('*', end='')
            else:
                print('0', end='')
            j += 1
        elif j == n + 1:
            print('*', end='')
            j += 1
        else:
            if a == j:
                print('*', end='')
                a -= 1
            else:
                print('0', end='')
            j += 1
    print()
    i += 1
