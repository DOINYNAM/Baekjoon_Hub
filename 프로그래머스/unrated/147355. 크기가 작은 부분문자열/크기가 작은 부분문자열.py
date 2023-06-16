def solution(t, p):
    answer = 0
    
    for i in range(0, len(t)) :
        target = t[i:i + len(p)]
        
        if len(target) == len(p) and int(target) <= int(p) :
            answer += 1
                   
    return answer