'''
Print Number Pyramid
Print the following pattern for a given n.
For eg. N = 6
123456
 23456
  3456
   456
    56
     6
    56
   456
  3456
 23456
123456
'''

n = int(input())

for i in range(0, 2 * n - 1):
    for j in range(1, n + 1):
        if i <= (2 * n - 1) // 2:
            if j <= i:
                print(' ', end='')
            if j > i:
                print(j, end='')
        if i > (2 * n - 1) // 2 and i <= 2 * n - 1:
            a = ((2 * n) - 2) - i
            if a >= j:
                print(' ', end='')
            if a < j:
                print(j, end='')
    print(' ', end='')
    print(i)
