x, y, w, h = list(map(int, input().split()))

best = 500

if abs(x - w) < best:
    best = abs(x - w)
if abs(y - h) < best:
    best = abs(y - h)
if abs(x) < best:
    best = x
if abs(y) < best:
    best = y

print(best)
