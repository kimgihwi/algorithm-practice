import sys

N = int(input())

#
# for _ in range(N):
#     num_list.append(int(input()))

num_list = [int(sys.stdin.readline().strip()) for i in range(N)]

num_list.sort()

many_num = 0
many_num_list = []
best = 0
tmp = 0
cur = num_list[0]

for idx in range(N):
    if cur != num_list[idx]:
        cur = num_list[idx]
        tmp = 1
        if tmp == best:
            many_num_list.append(cur)
        elif tmp > best:
            best = tmp
            many_num_list = [cur]
    else:
        tmp += 1
        if tmp == best:
            many_num_list.append(cur)
        elif tmp > best:
            best = tmp
            many_num_list = [cur]

print(round(sum(num_list) / N))
print(num_list[N // 2])
if len(many_num_list) == 1:
    print(many_num_list[0])
else:
    print(many_num_list[1])
print(num_list[-1] - num_list[0])
