T = int(input())


def floor(a, b):
    # if a == 0:
    #     return b
    # total = 0
    # for i in range(b):
    #     total += floor(a-1, i+1)
    # return total
    # if a == 0:
    #     for b_ in range(b):
    #         memo.append(b_)
    #     print(memo)
    #
    # else:
    #     print(1)
    #     for b_ in range(b):
    #         memo.append(sum(memo[:a*b+b_]))
    memo = list(range(1, b+1))
    if b != 0:
        for a_ in range(a):
            for b_ in range(b):
                memo.append(sum(memo[a_*b:a_*b+b_+1]))

    return memo[-1]


for _ in range(T):
    k = int(input())
    n = int(input())
    print(floor(k, n))


# print(floor(0, 3))
# print(floor(1, 3))
# print(floor(2, 4))
#
# for _ in range(T):
#     a = int(input())
#     b = int(input())
#     print(floor(a, b))
