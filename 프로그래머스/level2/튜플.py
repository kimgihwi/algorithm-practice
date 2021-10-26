def solution(s):

    s_ = s[2:-2]
    s_ = s_.split("},{")

    s_list = []

    for i in s_:
        s_list.append(i.split(','))

    s_len = len(s_list)
    answer = []

    s_list.sort(key=len)

    for j in range(s_len):
        tmp = [int(x) for x in s_list[j]]
        for n in answer:
            if n in tmp:
                tmp.remove(n)
        answer.append(tmp[0])

    return answer


if __name__ == '__main__':
    print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
    print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
    print(solution("{{20,111},{111}}"))
    print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))