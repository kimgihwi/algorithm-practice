def solution(n):

    nums = [x for x in range(2, n+1)]
    root = [x for x in range(2, int(n*0.5)+1)]
    answer = 0

    for root_ in root:
        if root_ in nums:
            nums.remove(root_)
        else:
            continue
        for num in nums:
            if num % root_ == 0:
                nums.remove(num)
        answer += 1
    return answer + len(nums)


if __name__ == '__main__':
    print(solution(10))
    print('_'*10)
    print(solution(5))
