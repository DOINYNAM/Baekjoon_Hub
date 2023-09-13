def solution(n, lost, reserve):
    
    # 공통 요소를 제거한 차집합 리스트 생성
    n_lost = sorted(list(set(lost) - set(reserve)))
    n_reserve = sorted(list(set(reserve) - set(lost)))
    
    # 체육복 빌려주기
    for i in n_reserve:
        if i-1 in n_lost: # 앞 번호 확인
            n_lost.remove(i-1)
            
        elif i+1 in n_lost: # 뒷 번호 확인
            n_lost.remove(i+1)
            
    return n - len(n_lost)