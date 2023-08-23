def solution(a, b, n):
    coke = 0 # 콜라 개수 cnt
    btl = n # 빈병 개수 cnt
    
    while True:
        coke += (btl // a) * b # 가진 빈병으로 받을 수 있는 콜라 개수 계산
        btl = (btl % a) + (btl // a) * b # 사용 후 남은 빈병 수 + 얻은 콜라 개수 계산
        
        if btl < a: # 남은 빈병 개수가 콜라를 받을 수 있는 빈병 수 보다 적어질 때 까지 실행
            break
            
    return coke