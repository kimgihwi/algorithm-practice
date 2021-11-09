# TODO 효율성 올리기
def solution(number, k):

    k_ = len(number) - k
    answer = ''
    number_ = [x for x in number]
    while k_>0:
        tmp_idx = find(number_, k_)
        answer += str(number_[tmp_idx])
        number_ = [x_ for x_ in number_[tmp_idx+1:]]
        k_ -=1

    return answer


def find(number, k):
    if k == 1:
        number_ = number
    else:
        number_ = number[:-k+1]
    number_ = list(number_)
    max_num = max(number_)
    max_idx = number_.index(max_num)

    return max_idx


if __name__ == '__main__':
    print(solution("1924", 2))
    print(solution("1231234", 3))
    print(solution("4177252841", 4))
    print(solution("9"*1000000, 99999))
