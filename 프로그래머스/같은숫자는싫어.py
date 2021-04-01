def solution(arr):

    if len(arr) == 1:
        return arr

    answer = [arr[0]]

    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i+1])

    return answer

if __name__ == '__main__':
    print(solution([1,1,3,3,0,1,1]))
    print(solution([4,4,4,3,3]))