'''
Code : Diamond of stars
Print the following pattern for the given number of rows.
Note: N is always odd.
Pattern for N = 5
   *
  ***
 *****
  ***
   *
'''

# # n = int(input())

# # i = 1
# # while i <= n:
# #     if i <= n//2 + 1:
# #         j = 1
# #         while j <= n - i:
# #             print(' ', end='')
# #             j += 1
# #         stars = 1
# #         while stars <= i:
# #             print('*', end='')
# #             stars += 1
# #         a = 1
# #         while a <= i - 1:
# #             print('*', end='')
# #             a += 1
# #         print()
# #         i += 1
# #     else:
# #         j = 1
# #         while j <= i % (n//2 + 1):
# #             print(' ', end='')
# #             j += 1
# #         stars -= 2
# #         a = 1
# #         while a <= stars:
# #             print('*', end='')
# #             a += 1
# #         print()
# #         i += 1


n = int(input())

i = 1
spaces = 1
while i <= (n//2 + 1):
    stars = 1
    j = i
    while (n//2 + 1) - j > 0:
        print(' ', end='')
        j += 1
    while stars <= 2 * i - 1:
        print('*', end='')
        stars += 1
    print()
    i += 1
    stars = n - 2
while i > (n//2 + 1) and i <= n:
    a = i
    while a - (n//2 + 1) >= 1:
        # print('a - (n//2 + 1) = ', a - (n//2 + 1))
        print(' ', end='')
        a -= 1
    star = 1
    while star <= stars:
        print('*', end='')
        star += 1
    stars -= 2
    print()
    i += 1
