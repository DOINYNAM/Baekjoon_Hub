def solution(n, times):
    # right는 가장 비효율적으로 심사했을 때 걸리는 시간
    # 가장 긴 심사시간이 소요되는 심사관에게 n 명 모두 심사받는 경우
    start = min(times)
    end = max(times)*n

    while start <= end:
        mid = (start + end) // 2
        checked = 0 # checked는 모든 심사관들이 mid분 동안 심사한 사람의 수

        for time in times:
            checked += mid // time 
            # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상의 심사를 할 수 있다면 반복문을 나간다.
            if checked >= n:
                break
        
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 적은 경우
        if checked < n:
            start = mid + 1
            
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우
        elif checked >= n:
            end = mid - 1
            
    return start