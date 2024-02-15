# 백준 15961 회전 초밥
# 슬라이딩 윈도우
import sys
from collections import defaultdict
input = sys.stdin.readline

# 입력 처리 -> 초밥 벨트 위 접시 수, 초밥 종류 수, 연속해서 먹는 수, 쿠폰 번호
n, d, k, c = map(int, input().split())
sushi = [int(input ().strip()) for _ in range(n)]

# 슬라이딩 윈도우 및 초밥 종류 카운팅을 위한 딕셔너리 준비
sushi_kind = defaultdict(int)
sushi_kind[c] = 1  # 쿠폰 초밥은 항상 포함

# 초기 윈도우 설정
for i in range(k):
    sushi_kind[sushi[i]] += 1
max_kind = len(sushi_kind)

# 슬라이딩 윈도우 실행
for i in range(1, n):
    left = i - 1
    right = (i + k - 1) % n # 인덱스가 다시 0으로 돌아오도록 %n
    sushi_kind[sushi[left]] -= 1

    if sushi_kind[sushi[left]] == 0:
        del sushi_kind[sushi[left]]

    sushi_kind[sushi[right]] += 1
    max_kind = max(max_kind, len(sushi_kind))

print(max_kind)