# 백준 16401 과자 나눠주기
# 이분 탐색
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
snacks = list(map(int, input().split()))

start = 1
end = max(snacks)

while start <= end:
  mid = (start + end) // 2 # 첫 기준 과자 길이 설정
  tmp = sum(i // mid for i in snacks) # 각 과자를 기준으로 mid 길이로 나눈 개수 저장

  if tmp >= M: # 과자의 개수가 많거나 충분할 때
    start = mid + 1

  else: # 과자의 개수가 모자를 때
    end = mid - 1

print(end)