n = int(input())

result = []


def score():
    question = input()
    total = 0
    current = 0

    for q in question:
        if q == 'O':
            current += 1
            total += current
        else:
            current = 0

    return total


for i in range(n):
    print(score())
