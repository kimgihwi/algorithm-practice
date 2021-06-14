def solution():
    h_num, p_num = list(map(int, input().split()))

    truth_h = [False] * (h_num + 1)
    truth_p = [False] * (p_num + 1)

    truth_ = list(map(int, input().split()))

    if truth_[0] == 0:
        return p_num

    if len(truth_) == h_num:
        return 0

    for t in truth_[1:]:
        truth_h[t] = True

    party = []

    for i in range(p_num):
        tmp_ = list(map(int, input().split()))
        party.append(tmp_[1:])

    while True:
        tmp = [x for x in truth_p]

        for idx in range(p_num):
            if truth_p[idx+1]:
                continue

            for h in party[idx]:
                if truth_h[h]:
                    for h_ in party[idx]:
                        truth_h[h_] = True
                    truth_p[idx+1] = True

        if tmp == truth_p:
            break

    return truth_p.count(False) - 1


print(solution())
