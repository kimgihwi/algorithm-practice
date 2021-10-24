N, M = list(map(int, input().split()))

num = list(map(int, input().split()))

best = -1

for n1 in num:
    tmp_num1 = [x for x in num]
    tmp_num1.remove(n1)
    for n2 in tmp_num1:
        tmp_num2 = [x for x in tmp_num1]
        tmp_num2.remove(n2)
        for n3 in tmp_num2:
            tmp = n1 + n2 + n3
            if tmp > best and tmp <= M:
                best = tmp

print(best)
