import sys
from collections import deque

def bfs(N, K):  # K를 매개변수로 추가했습니다.
    # 방문한 위치를 기록할 배열, 최대 위치 가정
    visited = [0] * 100001
    # 큐 초기화 및 시작 위치 추가
    queue = deque([N])  # 현재 위치

    while queue:
        cur_pos = queue.popleft()

        # 현재 위치가 K면 현재 시간 반환
        if cur_pos == K:
            return visited[cur_pos]

        # 걷기 or 순간이동으로 이동할 수 있는 위치 계산
        next_positions = [cur_pos - 1, cur_pos + 1, cur_pos * 2]

        for next_pos in next_positions:
            # 다음 위치가 유효 범위 내에 있고, 아직 방문 전이면
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = visited[cur_pos] + 1  # 현재 위치에서 1 추가
                queue.append(next_pos)

# 입력 받기
input = sys.stdin.readline
N, K = map(int, input().split())
print(bfs(N, K))