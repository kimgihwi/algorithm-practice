N = int(input())

word = []

for _ in range(N):
    word.append(input())

word = list(set(word))
word.sort()

answer = []
cnt = 1
while cnt < 51:
    word_ = word.copy()
    for w in word_:
        if len(w) == cnt:
            answer.append(w)
            word.remove(w)
    cnt += 1

for a in answer:
    print(a)

if len(word) == 1:
    print(word[0])
