def prime_Factorization(N):

    d = 2
    fac = []

    while N > 1:
        if N % d == 0:
            fac.append(d)
            N /= d
        else:
            d = d + 1

    return fac


n, m = list(map(int, input().split()))

n_f = prime_Factorization(n)
m_f = prime_Factorization(m)

u_f = list(set(n_f + m_f))

gcd = 1
lcm = 1

for u in u_f:
    n_ = n_f.count(u)
    m_ = m_f.count(u)
    gcd *= u**min(n_, m_)
    lcm *= u**max(n_, m_)

print(gcd)
print(lcm)
