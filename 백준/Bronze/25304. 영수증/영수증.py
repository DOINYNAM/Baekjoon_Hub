total_price = int(input())
items_num = int(input())
temp_total_price = 0

for _ in range(items_num):
  price, num = map(int, input().split())
  temp_total_price += price * num

if temp_total_price == total_price:
  print("Yes")

else:
  print("No")