'''
Print the pattern
Print the following pattern for the given number of rows.
Pattern for N = 5
 1    2   3    4   5
 11   12  13   14  15
 21   22  23   24  25
 16   17  18   19  20
 6    7    8   9   10
Input format : N (Total no. of rows)
Output format : Pattern in N lines
'''

n = int(input())

if n % 2 == 0:
        N = n / 2
        a1 = int(N) 
else:
        N = (n // 2) + 1
        a1 = N
        
a = 0
for i in range(1, n + 1):
        if i <= N:
                for j in range(1, n + 1):
                        #print(a, end = '')
                        print(str((n * a) + j) + ' ', end = '')
                if i != N:
                        a += 2
                if a % 2 == 0:
                        a1 = a - 1
                else:
                        a1 = a + 1
        if i > N and i <= n:
                for j in range(1, n + 1):
                        #print(a1, end = '')
                        print(str((n * a1) + j) + ' ', end = '')
                a1 -= 2
        print()
            
