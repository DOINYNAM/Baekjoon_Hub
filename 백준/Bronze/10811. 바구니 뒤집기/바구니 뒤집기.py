N, M = map(int, input().split())

ball_dic = {i+1:i+1 for i in range(N)}

for _ in range(M):
  i, j = map(int, input().split())
  range_value_list = [ball_dic[k] for k in range(i, j+1)][::-1]

  for n, k in enumerate(range(i, j+1)):
    ball_dic[k] = range_value_list[n]

value_list = [str(k) for k in list(ball_dic.values())]
print(" ".join(value_list))