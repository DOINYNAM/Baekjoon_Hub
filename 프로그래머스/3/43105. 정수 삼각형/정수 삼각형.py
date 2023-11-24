def solution(triangle):
    # 바텀업?, 층과 개수는 동일
    # 0을 추가하지 않음
    for i in range(1, len(triangle)): # i = 몇번째 줄인지
        for j in range(i+1): # j = 줄 안에서 인덱스
            if j == 0: # 가장 왼쪽인 경우
                triangle[i][j] += triangle[i-1][j]
            elif j == i: # 가장 오른쪽인 경우
                triangle[i][j] += triangle[i-1][-1]
            else: # 가운데인 경우
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
                
    return max(triangle[-1])

# 0을 추가함
def solution(triangle):
    triangle = [[0] + line + [0] for line in triangle]
    
    for i in range(1, len(triangle)):
        for j in range(1, i+2):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
            
    return max(triangle[-1])