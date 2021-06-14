def fibo1(n):

    cashe = [0]*(n+1)

    def oper(n):
        if n < 2:
            return n
        else:
            return cashe[n-1] + cashe[n-2]

    for i in range(n+1):
        cashe[i] = oper(i)

    return cashe[n]


def fibo2(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x+y
    return x


def fibo3(n):

    def mat(m1, m2):
        r1l1 = m1[0][0] * m2[0][0] % 1000000007 + m1[0][1] * m2[1][0] % 1000000007
        r1l2 = m1[0][0] * m2[0][1] % 1000000007 + m1[0][1] * m2[1][1] % 1000000007
        r2l1 = m1[1][0] * m2[0][0] % 1000000007 + m1[1][1] * m2[1][0] % 1000000007
        r2l2 = m1[1][0] * m2[0][1] % 1000000007 + m1[1][1] * m2[1][1] % 1000000007
        return [[r1l1, r1l2], [r2l1, r2l2]]

    if n == 0:
        return 0

    elif n < 3:
        return 1

    matrix = [[1, 1], [1, 0]]

    for i in range(n-2):
        matrix = mat(matrix, [[1, 1], [1, 0]])

    return matrix[0][0]


if __name__ == '__main__':
    N = int(input())
    print(fibo3(N) % 1000000007)
