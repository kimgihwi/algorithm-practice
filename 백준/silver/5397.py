#TODO: 백준 index error 해결

n = int(input())

answer = []

for n_ in range(n):
    key = list(input())

    idx = 0
    result = []

    for k in key:

        if k == '<':
            if idx > 0:
                idx -= 1
        elif k == '>':
            if idx < len(result):
                idx += 1
        elif k == '-':
            if len(result) > 0:
                result.pop(idx-1)
                idx -= 1
        else:
            result.insert(idx, k)
            idx += 1
        print(idx, result)

    answer.append(''.join(result))

for a in answer:
    print(a)
