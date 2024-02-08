# 백준 2583 영역 구하기
# dfs
import sys

sys.setrecursionlimit(10000)  # 재귀 깊이 제한 설정
input = sys.stdin.readline

# 입력 받기
M, N, K = map(int, input().split())  # M: 세로 크기, N: 가로 크기, K: 직사각형의 개수
grid = [[0] * N for _ in range(M)]  # 격자 초기화

# 직사각형을 격자에 표시
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            grid[i][j] = 1  # 직사각형 영역을 1로 표시

# DFS 함수 정의
def dfs(x, y):
    if x < 0 or y < 0 or x >= M or y >= N or grid[x][y] != 0:
        return 0  # 격자 범위를 벗어나거나 이미 방문했거나 직사각형 영역인 경우
    grid[x][y] = 1  # 현재 칸 방문 처리
    area = 1  # 현재 칸을 포함하여 영역의 크기를 1로 시작
    # 상하좌우 탐색
    area += dfs(x-1, y)
    area += dfs(x+1, y)
    area += dfs(x, y-1)
    area += dfs(x, y+1)
    return area  # 탐색이 끝난 후 영역의 크기 반환

# 각 영역의 크기를 저장할 리스트
areas = []

# 격자 전체를 탐색하며 영역 찾기
for i in range(M):
    for j in range(N):
        if grid[i][j] == 0:  # 아직 방문하지 않은 빈 영역인 경우
            areas.append(dfs(i, j))  # DFS를 통해 영역의 크기를 구하고 리스트에 추가

# 결과 출력
areas.sort()  # 영역의 크기를 오름차순으로 정렬
print(len(areas))  # 영역의 개수 출력
print(' '.join(map(str, areas)))  # 각 영역의 크기를 공백으로 구분하여 출력