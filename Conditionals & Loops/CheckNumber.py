S = int(input())
E = int(input())
W = int(input())

while S <= E:
    C = (S - 32) * 5//9
    print(str(S) + ' ' + str(C))
    S = S + W
