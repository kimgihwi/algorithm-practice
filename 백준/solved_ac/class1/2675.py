N = int(input())

for i in range(N):
    n, s = list(input().split(' '))
    word = ''
    for s_ in s:
        word += s_*int(n)
    print(word)