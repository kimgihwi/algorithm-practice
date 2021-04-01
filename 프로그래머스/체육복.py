def solution(n, lost, reserve):

    answer = n - len(lost)

    # for i in lost:
    #     if i-1 in reserve:
    #         answer += 1
    #         reserve.remove(i-1)
    #     elif i in reserve:
    #         answer += 1
    #         reserve.remove(i)
    #     elif i+1 in reserve:
    #         answer += 1
    #         reserve.remove(i+1)

    tmp_lost = [x for x in lost]

    for j in tmp_lost:
        if j in reserve:
            answer += 1
            reserve.remove(j)
            lost.remove(j)

    if len(lost) == 0 or len(reserve) == 0:
        return answer

    for i in lost:
        if i - 1 in reserve:
            answer += 1
            reserve.remove(i - 1)
        elif i + 1 in reserve:
            answer += 1
            reserve.remove(i + 1)

    return answer


if __name__ == '__main__':
    print(solution(5, [2, 4], [1, 3, 5]))
    print(solution(5, [2, 4], [3]))
    print(solution(3, [3], [1]))
    print(solution(10, [1, 3], [1, 3]))
