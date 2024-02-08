n = int(input())  # NxN 격자의 크기 입력 받음
students = {}  # 각 학생의 선호하는 학생 목록을 저장할 딕셔너리
board = [[0] * n for _ in range(n)]  # 학생들을 배치할 격자판 초기화

# 주변 4방향을 탐색하기 위한 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 선호하는 학생 수와 빈 자리 수에 따라 자리를 정하는 함수
def find_seat(favs):
    max_like, max_empty, pos = -1, -1, (-1, -1)
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:  # 빈 자리인 경우에만 탐색
                like_cnt, empty_cnt = 0, 0
                for i in range(4):  # 주변 4방향 탐색
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] in favs:
                            like_cnt += 1
                        elif board[nx][ny] == 0:
                            empty_cnt += 1
                # 최적의 자리를 찾는 조건 비교
                if like_cnt > max_like or (like_cnt == max_like and empty_cnt > max_empty) or \
                   (like_cnt == max_like and empty_cnt == max_empty and x < pos[0]) or \
                   (like_cnt == max_like and empty_cnt == max_empty and x == pos[0] and y < pos[1]):
                    max_like, max_empty, pos = like_cnt, empty_cnt, (x, y)
    return pos

# 학생 정보 입력 받아서 처리
for _ in range(n**2):
    info = list(map(int, input().split()))
    student, favs = info[0], info[1:]
    students[student] = favs
    x, y = find_seat(favs)  # 학생을 배치할 자리 찾기
    board[x][y] = student  # 학생 배치

# 만족도 계산 함수
def calc_satisfaction():
    satisfaction = 0
    for x in range(n):
        for y in range(n):
            like_cnt = 0
            for i in range(4):  # 주변 4방향 탐색
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] in students[board[x][y]]:
                        like_cnt += 1
            # 만족도에 따라 점수 부여
            if like_cnt > 0:
                satisfaction += 10**(like_cnt - 1)
    return satisfaction

# 최종 만족도 계산
print(calc_satisfaction())