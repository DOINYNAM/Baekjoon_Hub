# 목적 좌표에 도달하는 경우의 수 계산 함수
def result(n, m): 
  dp = [[0] * m for _ in range(n)]
  for row in range(n):
    for col in range(m):
      if row == 0 or col == 0: # 첫 행, 열을 1로 채우기
        dp[row][col] = 1
      else:
        dp[row][col] = dp[row - 1][col] + dp[row][col - 1] # 해당 칸을 왼쪽과 위쪽칸의 수를 더해 채우기
  
  return dp[n - 1][m - 1]

# 실행 부분
n, m, k = map(int, input().split())
if k == 0: # 원이 없는 경우
  print(result(n, m))

else: # 원이 있는 경우
  x, y = k // m + 1, k % m # 원이 있는 지점의 좌표 구하기
  n, m = (n + 1) - x, (m + 1) - y # 원이 있는 지점 이후부터 목적 좌표까지의 좌표 크기 재설정
  dp1, dp2 = result(x, y), result(n, m)
  
  print(dp1 * dp2) # 원이 있는 지점까지 도달하는 경우의 수  * 원이 있는 지점 제외 도달하는 경우의 수 = 원 좌표를 포함한 목적 좌표까지 도달하는 경우의 수