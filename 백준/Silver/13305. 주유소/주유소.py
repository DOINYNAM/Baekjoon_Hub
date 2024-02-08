# 백준 13305 주유소
# 그리디
import sys
input = sys.stdin.readline

# 도시의 개수 입력
N = int(input())

# 각 도시를 연결하는 도로의 길이 입력
distances = list(map(int, input().split()))

# 각 도시의 주유소 기름 가격 입력
prices = list(map(int, input().split()))

# 첫 번째 도시의 가격을 최소 가격으로 초기 설정
min_price = prices[0]

# 총 비용을 저장할 변수 초기화
total_cost = 0

# 모든 도시를 순회하면서 최소 비용 계산
for i in range(N-1):
    # 현재 도시의 기름 가격이 이전 도시의 기름 가격보다 싸면, 최소 가격 업데이트
    if prices[i] < min_price:
        min_price = prices[i]
    # 최소 가격으로 현재 도로의 길이만큼 주유
    total_cost += min_price * distances[i]

# 총 비용 출력
print(total_cost)