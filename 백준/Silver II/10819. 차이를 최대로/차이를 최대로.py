# 백준 10819 차이를 최대로
# 브루트 포스
# 순열(permutations)

import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())  # 배열의 크기 입력
arr = list(map(int, input().split()))  # 배열 입력

max_sum = 0  # 차이의 합의 최댓값을 저장할 변수 초기화

# arr의 모든 순열에 대해 반복
for perm in permutations(arr):
    # 현재 순열의 연속된 요소들의 차이의 절댓값의 합 계산
    current_sum = sum(abs(perm[i] - perm[i+1]) for i in range(n-1))
    
    # 계산된 합이 현재 최댓값보다 크면 최댓값 갱신
    max_sum = max(max_sum, current_sum)

# 차이의 합의 최댓값 출력
print(max_sum)