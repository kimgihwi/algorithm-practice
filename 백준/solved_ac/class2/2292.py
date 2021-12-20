N = int(input())

n = 0

while True:
    n += 1
    if 3*(n-1)**2 - 3*n + 2 <= N <= 3*n**2 - 3*n + 1:
        break

print(n)
