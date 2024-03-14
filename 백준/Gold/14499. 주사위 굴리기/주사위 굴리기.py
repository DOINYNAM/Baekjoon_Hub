# 백준 14499 주사위 굴리기
import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0 for _ in range(7)]
n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))

for order in orders:
    order -= 1
    nx = x + dx[order]
    ny = y + dy[order]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    if order == 0:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif order == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif order == 2:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    else:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    if board[nx][ny] == 0:
        board[nx][ny] = dice[6]
    else:
        dice[6] = board[nx][ny]
        board[nx][ny] = 0
    x, y = nx, ny
    print(dice[1])