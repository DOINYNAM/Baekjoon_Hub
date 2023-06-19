def solution(cards1, cards2, goal):
    cards1_dic = {value:i for i, value in enumerate(cards1)}
    cards2_dic = {value:i for i, value in enumerate(cards2)}
    cards1_cnt, cards2_cnt = 0, 0
    
    for l in range(len(goal)):
        key_word = goal[l]
        
        if key_word in cards1_dic and cards1_dic[key_word] == cards1_cnt:
            cards1_cnt += 1
            
            
        elif key_word in cards2_dic and cards2_dic[key_word] == cards2_cnt:
            cards2_cnt += 1
            
        else:
            result = "No"
            break
        
        result = "Yes"
    
    return result