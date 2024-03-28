# 백준 1025 제곱수 찾기
import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())  # 격자의 크기
grid = [input() for _ in range(N)]  # 격자 정보

# 제곱수인지 판별하는 함수
def is_square(n):
    return int(n**0.5) ** 2 == n

# 최댓값 초기화
max_square = -1

# 격자판의 모든 위치를 시작점으로 순회
for start_i in range(N):
    for start_j in range(M):
        # 가능한 모든 방향과 간격으로 숫자 이어붙이기
        for di in range(-N, N):
            for dj in range(-M, M):
                if di == 0 and dj == 0:  # 방향이 없는 경우는 제외
                    continue
                i, j = start_i, start_j  # 시작 위치
                num_str = ''  # 이어 붙인 숫자를 문자열로 저장
                # 격자판의 범위를 벗어날 때까지 숫자 이어붙이기
                while 0 <= i < N and 0 <= j < M:
                    num_str += grid[i][j]  # 숫자 이어붙이기
                    if is_square(int(num_str)):  # 제곱수인지 확인
                        max_square = max(max_square, int(num_str))  # 최댓값 업데이트
                    i += di  # 다음 위치로 이동
                    j += dj

# 결과 출력
print(max_square)