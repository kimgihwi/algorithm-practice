N, M = list(map(int, input().split()))

chess = []
for _ in range(N):
    tmp = input()
    chess.append(tmp)

# W_answer = []
# B_answer = []

# for i in range(8):
#     if i % 2 == 0:
#         W_answer.append('WB'*4)
#         B_answer.append('BW'*4)
#     else:
#         W_answer.append('BW'*4)
#         B_answer.append('WB'*4)

# x, y = 0, 0
best = 50*50

for x_ in range(N-7):
    for y_ in range(M-7):
        tmp = 0
        # if chess[x_][y_] == 'W':
        #     C_answer = W_answer
        # else:
        #     C_answer = B_answer
        #
        # first, second = C_answer[0], C_answer[1]
        # print(chess[0][0], chess[0][0]=='W')
        # if chess[x_][y_] == 'W':
        #     for n in range(8):
        #         for m in range(8):
        #             if (n + m) % 2 == 0:
        #                 if chess[x_+n][y_+m] == 'W':
        #                     continue
        #                 else:
        #                     tmp += 1
        #             else:
        #                 if chess[x_+n][y_+m] == 'B':
        #                     continue
        #                 else:
        #                     tmp += 1
        # else:
        #     for n in range(8):
        #         for m in range(8):
        #             if (n + m) % 2 == 0:
        #                 if chess[x_+n][y_+m] == 'B':
        #                     continue
        #                 else:
        #                     tmp += 1
        #             else:
        #                 if chess[x_+n][y_+m] == 'W':
        #                     continue
        #                 else:
        #                     tmp += 1
        for n in range(8):
            for m in range(8):
                if (n + m) % 2 == 0:
                    if chess[x_+n][y_+m] == 'W':
                        continue
                    else:
                        tmp += 1
                else:
                    if chess[x_+n][y_+m] == 'B':
                        continue
                    else:
                        tmp += 1

        if tmp < best:
            best = tmp

        tmp = 0

        for n in range(8):
            for m in range(8):
                if (n + m) % 2 == 0:
                    if chess[x_+n][y_+m] == 'B':
                        continue
                    else:
                        tmp += 1
                else:
                    if chess[x_+n][y_+m] == 'W':
                        continue
                    else:
                        tmp += 1

        if tmp < best:
            best = tmp

print(best)
