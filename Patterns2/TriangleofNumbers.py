'''
Code : Triangle of Numbers
Send Feedback
Print the following pattern for the given number of rows.
Pattern for N = 4
   1
  232
 34543
4567654
'''
# n = int(input())

# i = 1
# while i <= n:
#     spaces = 1
#     while spaces <= n - i:
#         print(' ', end='')
#         spaces += 1
#     a = 1
#     b = i
#     while a <= i:
#         print(b, end='')
#         b += 1
#         a += 1
#     while b >= i:
#         print(b, end='')
#         b -= 1
#     i += 1
#     print()

n = int(input())

i = 1
while i <= n:
    j = 1
    while j <= n - i:
        print(' ', end='')
        j += 1
    num = 1
    a = i
    while num <= i:
        print(a, end='')
        a += 1
        num += 1
    a -= 1
    while a > i:
        a -= 1
        print(a, end='')
    print()
    i += 1
