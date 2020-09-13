'''
Diamond of Stars
Print the following pattern for the given number of rows.
Note: N is always odd.
Pattern for N = 5
   *
  ***
 *****
  ***
   *
The dots represent spaces.
'''

n = int(input())
stars = 1
for i in range(1, n + 1):
    star = 1
    for j in range(1, n + 1):
        if i <= (n // 2) + 1:
            if ((n // 2) + 1) - i >= j:
                print(' ', end='')
            if ((n // 2) + 1) - i < j and star <= stars:
                print('*', end='')
                star += 1
    stars += 2
    if i > (n // 2) + 1 and i <= n:
        pass

    print()
