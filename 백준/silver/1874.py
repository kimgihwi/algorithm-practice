n = int(input())

seq = []

for i in range(n):
    seq.append(int(input()))

seq.reverse()
num = [x for x in range(1, n+1)]
num.reverse()
stack = []

answer=[]
yes = True

while len(seq)>0:
    ans_len = len(answer)
    if len(stack)==0:
        stack.append(num.pop())
        answer.append('+')
    if stack[-1] == seq[-1]:
        stack.pop()
        seq.pop()
        answer.append('-')
    else:
        if len(num) == 0:
            print('NO')
            yes = False
            break
        stack.append(num.pop())
        answer.append('+')

    if ans_len == len(answer):
        print('NO')
        yes = False
        break

if yes:
    for i in answer:
        print(i)

