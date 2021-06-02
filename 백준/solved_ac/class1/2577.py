A = int(input())
B = int(input())
C = int(input())

sum = A*B*C

num_list = list(str(sum))

for n in range(0, 10):
    print(num_list.count(str(n)))
