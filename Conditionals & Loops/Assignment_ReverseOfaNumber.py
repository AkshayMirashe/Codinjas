'''
Write a program to generate the reverse of a given number N. Print the corresponding reverse number.
Note : If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.
'''


def reverse(n):
    rev = 0
    while n != 0:  # Running loop till n != 0
        m = n % 10   # For unit place of n
        n = int(n / 10)  # To remove the decimal place digits
        rev = (rev * 10) + m
    return rev


n = int(input())
result = reverse(n)
print(result)
