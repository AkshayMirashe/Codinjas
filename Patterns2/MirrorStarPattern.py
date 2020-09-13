'''
Code : Mirror Number Pattern
Print the following pattern for the given N number of rows.
Pattern for N = 4
   *
  **
 ***
**** 
'''

n = int(input())

i = 1
while i <= n:
    spaces = 1
    while spaces <= n - i:
        print(' ', end='')
        spaces += 1
    stars = 1
    num = 1
    while stars < i:
        print('*', end='')
        stars += 1
        num += 1
    while num >= 1:
        print('*', end='')
        num -= 1
    i += 1
    print()
