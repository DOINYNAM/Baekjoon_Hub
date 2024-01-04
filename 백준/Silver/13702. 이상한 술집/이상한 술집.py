N, K = map(int, input().split())
btl = [int(input()) for _ in range(N)]

start = 1
end = max(btl)

while start <= end:
  mid = (start + end) // 2 # 첫 기준 ml 설정
  tmp = sum(i // mid for i in btl) # 각 주전자를 기준으로 mid 용량으로 따른 잔의 개수 저장

  if tmp >= K: # 잔의 개수가 많거나 충분할 때
    start = mid + 1

  else: # 잔의 개수가 모자를 때
    end = mid - 1

print(end)