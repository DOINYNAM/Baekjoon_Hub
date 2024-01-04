from collections import deque
from sys import stdin
input = stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    while queue:
        y, x = queue.popleft()
        graph[y][x] = '.'
        for l in range(4):
            yy = dy[l] + y
            xx = dx[l] + x
            if 0 <= xx < c and 0 <= yy < r and graph[yy][xx] == 'O':
                graph[yy][xx] = '.'
                # queue.append((yy, xx)) 연쇄반응이 없다.

def search(): # 폭탄의 위치 큐에 추가
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'O':
                queue.append((i, j))

def bombSet(): # '.' -> 'O'으로 셋팅
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '.':
                graph[i][j] = 'O'

r, c, n = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(input().strip()))
n=n-1

while n:
    queue = deque()
    search()
    bombSet()
    n -= 1
    if n == 0:
        break
    bfs()
    n -= 1

for g in graph:
    print(*g, sep='')