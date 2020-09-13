'''
Code : Star Pattern
Print the following pattern
Pattern for N = 4
   *
  ***
 *****
*******
The dots represent spaces.
'''

n = int(input())

i = 1
while i <= n:
    spaces = 1  # printing reverse pattern
    while spaces <= n - i:
        print(' ', end='')
        spaces += 1
    num = 1
    stars = 1
    while stars < i:
        print(stars, end='')
        stars += 1  # printing reverse pattern till here
        num += 1
    while num >= 1:
        print(num, end='')
        num -= 1
    print()
    i += 1
