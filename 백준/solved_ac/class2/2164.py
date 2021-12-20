def card(n_list):
    tmp = []
    if len(n_list) % 2 == 0:
        for idx in range(len(n_list)):
            if idx % 2 == 1:
                tmp.append(n_list[idx])
    else:
        for idx in range(len(n_list)-1):
            if idx % 2 == 1:
                tmp.append(n_list[idx])
        tmp.insert(0, n_list[-1])

    return tmp


N = int(input())
N = list(range(1, N + 1))

while len(N) > 1:
    N = card(N)

print(N[0])
