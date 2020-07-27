'''
Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121
'''


def checkPalindrome(num):
    rev = 0
    number = num
    while num != 0:
        m = num % 10
        num = int(num / 10)
        rev = (rev * 10) + m
        reverse = rev
    return reverse == number


num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
    print('true')
else:
    print('false')
