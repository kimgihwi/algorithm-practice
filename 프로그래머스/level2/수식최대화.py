def solution(expression):

    exp_list = []

    tmp = ''
    for n in expression:
        if 47 < ord(n) < 58:
            tmp += n
        else:
            exp_list.append(int(tmp))
            exp_list.append(n)
            tmp = ''
    exp_list.append(int(tmp))

    best = 0

    oper_ = ['+-*', '+*-', '-+*', '-*+', '*+-', '*-+']

    for o_ in oper_:
        first = cal(exp_list, o_[0])
        second = cal(first, o_[1])
        third = cal(second, o_[2])

        if best < abs(third[0]):
            best = abs(third[0])

    return best


def cal(exp, op):
    answer = []
    idx = 0
    while idx < len(exp):
        if exp[idx] == op:
            idx += 1
            left = answer.pop()
            right = exp[idx]
            answer.append(oper(op, left, right))
        else:
            answer.append(exp[idx])
        idx += 1

    return answer


def oper(op, left, right):
    if op == '*':
        return left*right
    elif op == '-':
        return left-right
    elif op == '+':
        return left+right
    else:
        return ValueError


if __name__ == '__main__':
    print(solution("100-200*300-500+20"))
    print(solution("50*6-3*2"))
