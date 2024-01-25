# 백준 2170 선 긋기
# 시작, 끝 지점 누적 기록
# 구간별 선 길이 계산
import sys
input = sys.stdin.readline

N = int(input())
lines = sorted([tuple(map(int, input().split())) for _ in range(N)])

len = 0
start = lines[0][0]
end = lines[0][1]

for i in range(1, N): # 각 튜플별 끝 지점 비교
  if end >= lines[i][1]: # start, end 지점이 해당 구간을 전부 포함
    continue

  elif lines[i][0] <= end < lines[i][1]: # start, end 지점이 해당 구간 사이에 존재
    end = lines[i][1] # R

  elif end < lines[i][0]: # start, end 지점과 해당 구간이 독립적
    len += end - start # 기존 start, end 구간의 길이 저장
    start = lines[i][0] # 새로운 start, end 구간 지정
    end = lines[i][1]

len += end - start
print(len)  