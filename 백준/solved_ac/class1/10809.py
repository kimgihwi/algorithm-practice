C = input()

alpha = []

for i in range(97, 123):
    alpha.append(chr(i))

answer = []
for a in alpha:
    try:
        answer.append(str(C.index(a)))
    except:
        answer.append(str(-1))

print(" ".join(answer))
