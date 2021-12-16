import math


def solution(w, h):

    total = w*h

    if w < h:
        w, h = h, w

    if h == 1:
        return 0

    if h == 2:
        return math.ceil(total - w//h)

    if w is h:
        return total - w




    # return total - h*(math.ceil(w/h))


#     total = w*h
#     h += 0.
#     w += 0.
#
#     slope = h/w
#
#     for x in range(int(w)):
#         y = linear(slope, x)
#         if y-int(y) != 0:
#             total -= 2
#
#     return total
#
#
# def linear(slope, x):
#     return slope*x


if __name__ == '__main__':
    print(solution(8, 12))
    print(solution(2, 2))
    print(solution(3, 2))
    print(solution(4, 2))
    print(solution(5, 2))
    print(solution(3, 3))
    print(solution(4, 3))
    print(solution(4, 4))
