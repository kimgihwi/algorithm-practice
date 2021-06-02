def solution(participant, completion):
    sort_p = participant
    sort_p.sort()
    sort_c = completion
    sort_c.sort()

    for i in range(len(completion)):
        if sort_p[i] != sort_c[i]:
            return sort_p[i]
    return sort_c[-1]

    return answer


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))