'''
Arrow pattern
Print the following pattern for the given number of rows.
Assume N is always odd.
Note : There is space after every star.
Pattern for N = 7
*
 * *
   * * *
     * * * *
   * * *
 * *
*
'''

# n = int(input())

# i = 1
# while i <= (n//2 + 1):
#     j = 1
#     while j <= i:
#         print(' ', end='')
#         j += 1
#     star = 1
#     while star <= i:
#         print('* ', end='')
#         star += 1
#     print()
#     j -= 2
#     star -= 2
#     i += 1
# while i > (n//2 + 1) and i <= n:
#     a = 1
#     while a <= n + 1 - i:
#         print(' ', end='')
#         a += 1
#     b = 1
#     while b <= n + 1 - i:
#         print('* ', end='')
#         star -= 1
#         b += 1
#     print()
#     i += 1

#  *
#   * *   OUTPUT OF ABOVE CODE || INCORRECT
#    * * *
#     * * * *
#    * * *
#   * *
#  *

# *
#  * *    REQUIRED PATTERN || CORRECT
#    * * *
#      * * * *
#    * * *
#  * *
# *

# n = int(input())

# i = 1
# while i <= n:
#     a = i
#     if i <= a:
#         if i == 1:
#             print('*')
#             i += 1
#         if i > 1 and i <= a:
#               while a - 2 > 0:
#               print(' a', end='')
#               a += 1
#         j = 1
#             while j <= a:
#                 print(' *', end='')
#                 j += 1
#     i += 1
n = int(input())

i = 1
while i <= n:
    a = i
    b = (n // 2) + 1
    if i <= b:
        if i == 1:
            # Why does I need not to increase "i" i.e. i += 1
            print('*', end='')
        if i > 1 and i <= b:
            while a - 2 > 0:
                print(' ', end='')
                a -= 1
            j = 1
            a = i
            while j <= a:
                print(' *', end='')
                j += 1
    if i > b and i <= n:
        a = n + 1 - i
        if i == n:
            print('*', end='')
        if i > b and i < n:
            while a - 2 > 0:
                print(' ', end='')
                a -= 1
            j = 1
            a = n + 1 - i
            while j <= a:
                print(' *', end='')
                j += 1
    print()
    i += 1
