def solution(a, b):

    if a == b:
        return a

    if a > b:
        a, b = b, a

    answer = 0
    for n in range(a, b+1):
        answer += n

    return answer