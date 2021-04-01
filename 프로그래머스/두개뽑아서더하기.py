def solution(numbers):
    results = []

    for i in range(len(numbers)):
        tmp_nums = [x for x in numbers]
        tmp_nums.pop(i)
        for j in tmp_nums:
            results.append(numbers[i] + j)

    answer = list(set(results))
    answer.sort()

    return answer
