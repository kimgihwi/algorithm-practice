def solution(s):

    s_list = s.split(" ")
    num_list = [int(x) for x in s_list]

    return str(min(num_list)) + " " + str(max(num_list))


if __name__ == '__main__':
    print(solution("1 2 3 4"))