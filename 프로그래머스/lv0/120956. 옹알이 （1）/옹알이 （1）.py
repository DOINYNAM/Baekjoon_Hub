def solution(babbling):
    pos_word = ["aya", "ye", "woo", "ma"]
    cnt = 0
    
    for i in babbling:
        for j in pos_word:
            if j in i:
                i = i.replace(j, " ")
                
        if i.isspace():
            cnt += 1
            
    return cnt