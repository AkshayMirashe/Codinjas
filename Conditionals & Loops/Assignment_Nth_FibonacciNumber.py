'''
Nth term of fibonacci series F(n) is calculated using following formula -
    F(n) = F(n-1) + F(n-2), 
    Where, F(1) = F(2) = 1
Provided N you have to find out the Nth Fibonacci Number.
'''

n = int(input())


def fibonacci(n):
    a = 1
    b = 1
    i = 2
    while i != n:
        i += 1
        c = b
        b = a + b
        a = c
    return b


ans = fibonacci(n)
print(ans)
