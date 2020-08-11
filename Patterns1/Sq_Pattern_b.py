'''
print
1234
1234
1234
1234
'''

n = int(input())

i = 1
while i <= n:
    j = 1
    while j <= n:
        print(j, end='')
        j += 1
    print()
    i += 1
