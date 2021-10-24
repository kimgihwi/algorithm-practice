n = int(input())

seq = []

for i in range(n):
    seq.append(int(input()))

stack = [0]

num = list(range(1, n+1))
num.reverse()

answer = []

