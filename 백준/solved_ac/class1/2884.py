H, M = list(map(int, input().split()))

if M < 45:
    M = M + 15
    if not H:
        H = 23
    else:
        H -=1
else:
    M -= 45

print(H, M)