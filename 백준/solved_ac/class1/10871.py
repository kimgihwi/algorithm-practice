N, X = list(map(int, input().split()))
A = list(map(int, input().split()))

answer = []

for a in A:
    if a < X:
        answer.append(str(a))

print(" ".join(answer))
