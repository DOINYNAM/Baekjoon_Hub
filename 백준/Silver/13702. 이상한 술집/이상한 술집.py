# 백준 13702 이상한술집
# 이분 탐색

# start, end는 ml 지표
# N 주전자 개수, K 친구들 수

N, K = map(int, input().split())
btl = [int(input()) for _ in range(N)]

start = 1
end = max(btl)

while start <= end:
  mid = (start + end) // 2 # 첫 기준 ml 설정
  tmp = 0 # mid 용량으로 따른 잔의 개수 저장
  
  for i in btl:
    tmp += i // mid # 각 주전자를 기준으로 mid 용량으로 따른 잔의 개수 저장

  if tmp >= K: # 잔의 개수가 많거나 충분할 때
    start = mid + 1
    answer = mid

  else: # 잔의 개수가 모자를 때
    end = mid - 1

print(answer)