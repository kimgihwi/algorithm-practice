while True:
    yes_no = True
    num = input()
    if num == '0':
        break
    len_num = len(num)

    for i in range(len_num//2):
        if num[i] != num[len_num-i-1]:
            yes_no = False

    if yes_no:
        print('yes')
    else:
        print('no')
