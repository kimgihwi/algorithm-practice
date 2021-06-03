num_list = []
for i in range(10):
    num_list.append(int(input()))

mod = [x % 42 for x in num_list]

print(len(set(mod)))
