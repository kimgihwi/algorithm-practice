def solution(n):

    three_num = ''

    while n > 2:
        three_num += str(n % 3)
        n = n//3
    three_num += str(n)

    ten_num = 0

    for i in range(len(three_num)):
        ten_num += int(three_num[i]) * (3**(len(three_num)-i-1))

    return ten_num


if __name__ == '__main__':
    print(solution(45))
    print(solution(125))
