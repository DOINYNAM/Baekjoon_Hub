# 백준 11265 끝나지 않는 파티
# time_map 만들기
# (조건문) 소요시간 >= 시작시간 : enjoy other party 출력
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 그래프 설정
time_map = [list(map(int, input().split())) for _ in range(N)]

# 최단 경로 - 플로이드 워셜 알고리즘
for k in range(N):
    for i in range(N):
        for j in range(N):
            if time_map[i][j] > time_map[i][k] + time_map[k][j]:
                time_map[i][j] = time_map[i][k] + time_map[k][j]

# 조건 탐색
for _ in range(M):
  A, B, C = map(int, input().split())

  if time_map[A - 1][B - 1] <= C :
    print("Enjoy other party")

  else:
    print("Stay here")