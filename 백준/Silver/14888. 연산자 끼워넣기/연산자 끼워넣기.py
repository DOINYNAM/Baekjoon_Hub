import sys
input = sys.stdin.readline

n = int(input())  # 숫자의 개수 입력 받음
numbers = list(map(int, input().split()))  # 숫자들 입력 받음
operators = list(map(int, input().split()))  # +, -, *, // 순으로 연산자 개수 입력 받음

# 최솟값과 최댓값을 초기화합니다. 여기서는 가능한 결과값의 범위를 고려하여 설정합니다.
min_value = float('inf')
max_value = float('-inf')

# dfs 함수 정의: 현재까지 계산한 결과와 사용한 연산자의 수를 인자로 받습니다.
def dfs(depth, total, plus, minus, multiply, divide):
    global min_value, max_value
    # 모든 숫자를 다 사용했을 경우, 최소값과 최대값을 갱신합니다.
    if depth == n:
        min_value = min(min_value, total)
        max_value = max(max_value, total)
        return

    # 각 연산자에 대해 재귀적으로 다음 숫자와 계산을 시도합니다.
    if plus:
        dfs(depth + 1, total + numbers[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - numbers[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * numbers[depth], plus, minus, multiply - 1, divide)
    if divide:
        # 나눗셈은 정수 나눗셈의 특성을 고려하여 처리합니다.
        if total >= 0:
            dfs(depth + 1, total // numbers[depth], plus, minus, multiply, divide - 1)
        else:
            dfs(depth + 1, -(-total // numbers[depth]), plus, minus, multiply, divide - 1)

# 첫 번째 숫자를 시작으로 dfs 탐색을 시작합니다.
dfs(1, numbers[0], operators[0], operators[1], operators[2], operators[3])

# 최소값과 최대값 출력
print(max_value)
print(min_value)