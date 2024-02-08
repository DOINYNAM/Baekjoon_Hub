# 백준 1965 상자넣기
# DP

import sys
input = sys.stdin.readline

# 상자의 개수 입력
n = int(input())

# 상자의 크기 입력
boxes = list(map(int, input().split()))

# DP 테이블 초기화: 각 상자를 마지막으로 하는 LIS의 최대 길이 저장
dp = [1] * n

# 모든 상자를 순회하며 DP 테이블 업데이트
for i in range(1, n):
    for j in range(i):
        # 현재 상자(i)가 이전 상자(j)보다 크면, LIS 업데이트 가능
        if boxes[i] > boxes[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# DP 테이블에서 가장 큰 값(최장 LIS 길이) 출력
print(max(dp))