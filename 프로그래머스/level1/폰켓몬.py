def solution(nums):

    len_catch = int(len(nums) / 2)

    unique = len(list(set(nums)))

    if unique < len_catch:
        return unique
    else:
        return len_catch
