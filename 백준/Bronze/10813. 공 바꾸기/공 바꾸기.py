n, m = map(int, input().split())
ball_num_dic = {i+1:i+1 for i in range(n)}

for _ in range(m):
  i, j = map(int, input().split())
  i_ball, j_ball = ball_num_dic[i], ball_num_dic[j]
  ball_num_dic[i] = j_ball
  ball_num_dic[j] = i_ball

value_list = [str(k) for k in list(ball_num_dic.values())]
print(" ".join(value_list))