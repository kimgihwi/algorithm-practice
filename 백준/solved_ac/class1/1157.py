a = list(input().upper())

best_cnt = -1
best_str = ''
over = False

for uni in set(a):
    num = a.count(uni)
    if num > best_cnt:
        best_cnt = num
        best_str = uni
        over = False
    elif num == best_cnt:
        over = True

if over:
    print('?')
else:
    print(best_str)
