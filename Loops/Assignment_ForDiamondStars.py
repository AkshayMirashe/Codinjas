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
N = (n // 2) + 1
for i in range(1, n + 1):
    if i <= N:
        for _ in range(1, N - i + 1):
            print(' ', end='')
        for _ in range(1, stars + 1):
            print('*', end='')
        stars += 2
        # The above stars+=2 was increasing count unnecessarily. Therefore, require to add if i == N, decrease stars by 2.
        if i == N:
            stars -= 2
    if i > N and i <= n:
        stars -= 2
        spaces = i - N
        for _ in range(1, spaces + 1):
            print(' ', end='')
        for _ in range(1, stars + 1):
            print('*', end='')
    print()
