'''
Write a program to input an integer N and print the sum of all its even digits and sum of all its odd digits separately.
Digits mean numbers, not the places! That is, if the given integer is "13245", even digits are 2 & 4 and odd digits are 1, 3 & 5.
'''

n = int(input())
evenSum = 0
oddSum = 0

while n != 0:
    m = n % 10
    n = int(n / 10)
    if m % 2 == 0:
        evenSum = evenSum + m
    else:
        oddSum = oddSum + m
print(str(evenSum) + ' ' + str(oddSum))
