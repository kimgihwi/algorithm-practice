def solution(answers):

    first = [x%5+1 for x in range(len(answers))]
    second = []
    in_num = [1, 3, 4, 5]
    nxt = 0
    for i in range(len(answers)):
        if i % 2 == 0:
            second.append(2)
        else:
            second.append(in_num[nxt % 4])
            nxt += 1
    in_num_2 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    third = [in_num_2[j%10] for j in range(len(answers))]

    correct = [0, 0, 0]

    for k in range(len(answers)):
        if first[k] == answers[k]:
            correct[0] += 1
        if second[k] == answers[k]:
            correct[1] += 1
        if third[k] == answers[k]:
            correct[2] += 1

    max_correct = max(correct)

    most_correct = [max_correct==correct[i] for i in range(3)]

    answer = []
    for m in range(3):
        if most_correct[m]:
            answer.append(m+1)

    return answer


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
