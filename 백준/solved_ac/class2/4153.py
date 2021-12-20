while True:
    side = list(map(int, input().split()))
    if sum(side) == 0:
        break
    side.sort()
    if side[2]**2 == side[0]**2 + side[1]**2:
        print('right')
    else:
        print('wrong')
