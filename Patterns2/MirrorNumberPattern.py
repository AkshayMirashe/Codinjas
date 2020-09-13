'''
Code : Mirror Number Pattern
Print the following pattern for the given N number of rows.
Pattern for N = 4
   1
  12
 123
1234
'''

n = int(input())

i = 1
while i <= n:
    spaces = 1
    while spaces <= n - i:
        print(' ', end='')
        spaces += 1
    numberCount = 1
    while numberCount <= i:
        print(numberCount, end='')
        numberCount += 1
    i += 1
    print()
