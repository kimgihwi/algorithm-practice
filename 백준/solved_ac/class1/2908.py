A, B = list(map(int, input().split()))

A = (A % 10) * 100 + (A % 100 - A % 10) + A // 100
B = (B % 10) * 100 + (B % 100 - B % 10) + B // 100

if A > B:
    print(A)
else:
    print(B)