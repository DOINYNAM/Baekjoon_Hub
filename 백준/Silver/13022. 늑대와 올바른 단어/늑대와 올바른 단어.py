def is_valid_wolf_sequence(s):
    i = 0
    n = len(s)
    
    while i < n:
        # 각 문자의 개수 초기화
        w_count, o_count, l_count, f_count = 0, 0, 0, 0
        
        # 'w'의 개수 세기
        while i < n and s[i] == 'w':
            w_count += 1
            i += 1
        # 'o'의 개수 세기
        while i < n and s[i] == 'o':
            o_count += 1
            i += 1
        # 'l'의 개수 세기
        while i < n and s[i] == 'l':
            l_count += 1
            i += 1
        # 'f'의 개수 세기
        while i < n and s[i] == 'f':
            f_count += 1
            i += 1
        
        # 검증: 'w', 'o', 'l', 'f'의 개수가 모두 동일해야 함
        if not (w_count == o_count == l_count == f_count > 0):
            return 0
        
        # 'wolf' 패턴이 반복되는 경우를 위해 반복문 계속 진행
        
    # 모든 검증을 통과했다면, 올바른 'wolf' 패턴
    return 1

# 입력 받기
s = input().strip()
# 결과 출력
print(is_valid_wolf_sequence(s))