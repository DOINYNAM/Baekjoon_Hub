num_dic = {i+1:i+1 for i in range(30)}

for i in range(28):
  del(num_dic[int(input())])

value_list = sorted(list(num_dic.values()))

print(value_list[0], value_list[1], sep = '\n')