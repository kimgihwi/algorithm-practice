N = int(input())

digit = 0

while N//(10**digit) > 0:
    digit += 1

cur = 0
n = [0 for _ in range(digit)]
while True:

    n[0] += 1
    for idx in range(digit):
        if n[idx] > 9:
            n[idx] = 0
            n[idx+1] += 1

    answer = 0
    for idx_ in range(digit):
        answer += n[idx_] * (10**idx_ + 1)

    if answer == N:
        answer = 0
        for i in range(digit):
            answer += n[i] * (10**i)
        break

    if N == sum([n[i]*(10**i) for i in range(digit)]):
        answer = 0
        break

print(answer)