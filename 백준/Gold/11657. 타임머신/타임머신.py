import sys
input = sys.stdin.read

def bellman_ford(n, edges, start):
    # 최단 거리 테이블을 무한대로 초기화
    dist = [float('inf')] * (n + 1)
    dist[start] = 0

    # 정점 수 - 1번 만큼 각 간선을 확인
    for i in range(n):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                # N번째 루프에서도 값이 갱신된다면 음의 사이클 존재
                if i == n - 1:
                    return -1

    return dist

def solve():
    input_data = input().split()
    n, m = int(input_data[0]), int(input_data[1])
    edges = []
    idx = 2
    for _ in range(m):
        a, b, c = int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])
        edges.append((a, b, c))
        idx += 3
    
    result = bellman_ford(n, edges, 1)

    if result == -1:
        print(-1)
    else:
        for d in result[2:]:
            print(d if d != float('inf') else -1)

solve()