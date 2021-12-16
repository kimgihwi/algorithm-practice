# @TODO ABAAAAAAAAABB일 때, 해결해보기
def solution(name):

    alpha = []
    for a in range(ord('A'), ord('Z')+1):
        alpha.append(chr(a))

    cur = 0

    answer = ['A' for x in name]

    name_r = list(name)
    name_l = list(name)

    total_r = 0
    total_l = 0

    while True:
        if name_r[cur] == 'A':
            if name_r == answer:
                break
            else:
                total_r += 1
                # if cur == len(name_r)-1:
                #     cur = 0
                # else:
                #     cur += 1
                cur += 1

        else:
            if alpha.index(name_r[cur]) > 13:
                total_r += len(alpha) - alpha.index(name_r[cur])
            else:
                total_r += alpha.index(name_r[cur])
            name_r[cur] = 'A'
            if name_r == answer:
                break
            # if cur == len(name_r)-1:
            #     cur = 0
            else:
                cur += 1
                total_r += 1

    cur = 0

    while True:
        if name_l[cur] == 'A':
            if name_l == answer:
                break
            else:
                total_l += 1
                if cur == 0:
                    cur = len(name_l)-1
                else:
                    cur -= 1
        else:
            if alpha.index(name_l[cur]) > 13:
                total_l += len(alpha) - alpha.index(name_l[cur])
            else:
                total_l += alpha.index(name_l[cur])
            name_l[cur] = 'A'
            if name_l == answer:
                break
            # if cur == 0:
            #     cur = len(name_l)-1
            else:
                cur -= 1
                total_l += 1

    return min(total_r, total_l)


if __name__ == '__main__':
    # print(solution('JEROEN'))
    print(solution('JAN'))