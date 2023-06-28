arr_list = []

for _ in range(9):
  arr_list.append(list(map(int, input().split())))

x, y, max  = 0, 0, -1

for i in range(9):
  for j in range(9):
    if arr_list[i][j] > max:
      max = arr_list[i][j]
      x, y = i+1, j+1

print(max)
print(x, y)