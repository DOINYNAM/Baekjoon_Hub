N, M = map(int, input().split())
fair_dic = {num:0 for num in range(1, N + 1)}

for i in  range(M):
  start, end, value = map(int, input().split())
  
  for j in range(start, end + 1):
    fair_dic[j] = value

value_list = [str(k) for k in list(fair_dic.values())]
print(" ".join(value_list))