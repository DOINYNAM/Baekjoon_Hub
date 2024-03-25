from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    answer = 0
    
    total_sum = sum(q1) + sum(q2)
    if total_sum % 2 == 0:
        target = total_sum // 2
        current_sum = sum(q1)
        
        while answer < len(queue1) * 3:  # 최대 횟수 조정
            if current_sum == target:
                return answer
            elif current_sum < target:
                if q2:  # q2가 비어있지 않은 경우에만
                    pop = q2.popleft()
                    q1.append(pop)
                    current_sum += pop
            else:  # current_sum > target
                if q1:  # q1이 비어있지 않은 경우에만
                    pop = q1.popleft()
                    q2.append(pop)
                    current_sum -= pop
            
            answer += 1
    else:
        return -1  # 전체 합이 홀수인 경우 -1 반환
    
    return -1  # 위 조건들을 만족하지 않는 경우 -1 반환