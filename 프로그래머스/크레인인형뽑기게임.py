def solution(board, moves):
    stack = []
    basket = []
    cnt = 0

    for i in range(len(board)):
        tmp_stack = []
        for j in range(len(board)-1, -1, -1):
            tmp_stack.append(board[j][i])
        stack.append(tmp_stack)

    for m in moves:
        if len(stack[m-1]) == 0:
            continue

        drop = stack[m-1].pop()
        if drop == 0:
            while drop == 0:
                if len(stack[m-1]) == 0:
                    break
                drop = stack[m-1].pop()

        if drop == 0:
            continue

        if len(basket) != 0:
            if basket[-1] == drop:
                basket.pop()
                cnt += 2
                continue

        # if len(stack[m-1]) == 0:
        #     continue
        basket.append(drop)

    return cnt


board_ = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves_ = [1,5,3,5,1,2,1,4]