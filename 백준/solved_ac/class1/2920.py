play = list(map(int, input().split()))

asc = list(range(1, 9))
des = asc[::-1]

if play == asc:
    print('ascending')
elif play == des:
    print('descending')
else:
    print('mixed')
