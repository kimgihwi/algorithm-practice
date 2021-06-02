def solution(seoul):
    for idx in range(len(seoul)):
        if seoul[idx] == 'Kim':
            return("김서방은 {idx}에 있다".format(idx=idx))

