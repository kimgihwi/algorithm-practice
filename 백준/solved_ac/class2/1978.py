def prime_number(N):
    prime = [2]
    if N == 2:
        return prime
    for n in range(3, N+1):
        tmp = True
        for p in prime:
            if n % p == 0:
                tmp = False
                break
        if tmp:
            prime.append(n)
    return prime


n = int(input())
m = list(map(int, input().split()))
prime = prime_number(max(m))
answer = 0

for m_ in m:
    if m_ in prime:
        answer += 1

print(answer)