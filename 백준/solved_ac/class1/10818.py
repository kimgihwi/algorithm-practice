n = int(input())

input_list = input().split(" ")

int_list = [int(x) for x in input_list]

int_list.sort()

print(int_list[0], int_list[-1])
