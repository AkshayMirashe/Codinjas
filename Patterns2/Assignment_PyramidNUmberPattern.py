'''
Pyramid Number Pattern
Print the following pattern for the given number of rows.
Pattern for N = 4
   1
  212
 32123
4321234
Input format : N (Total no. of rows)
Output format : Pattern in N lines
'''

n = int(input())

i = 1
while i <= n:
    j = 1
    while j <= n - i:   
        print(' ', end='')
        j += 1
    num = i
    while num >= 1:
        print(num, end='')
        num -= 1
    num += 2
    while num <= i:
        print(num, end='')
        num += 1
    print()
    i += 1
