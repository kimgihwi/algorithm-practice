# @TODO: 나중에 이진탐색으로 풀기

N = int(input())

N_list = list(map(int, input().split()))

M = int(input())

M_list = list(map(int, input().split()))

for m in M_list:
    if m in N_list:
        print(1)
    else:
        print(0)
#
# M_list_ = M_list.copy()
# N_list.sort()
# M_list.sort()
#
# answer = [-1 for _ in range(N)]
#
# n = 0
# m = 0
#
# while n < N:
#     print(n, m)
#     if N_list[n] < M_list[m]:
#         # print(0)
#         n += 1
#     elif N_list[n] > M_list[m]:
#         answer[M_list_.index(M_list[m])] = 0
#         print(M_list_.index(M_list[m]))
#         m += 1
#     else:
#         answer[M_list_.index(M_list[m])] = 1
#         print(M_list_.index(M_list[m]))
#         # print(1)
#         n += 1
#         m += 1
#
# for i in range(m, M):
#     answer[M_list_.index(M_list[i])] = 0
#
# for a in answer:
#     print(a)
