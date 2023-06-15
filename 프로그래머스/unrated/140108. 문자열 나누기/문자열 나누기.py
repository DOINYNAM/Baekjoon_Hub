def solution(s):
    split_text = []
    result = []
    s_cnt = 1
    
    for i in range(len(s)):
        if s_cnt != 0:
            
            if len(split_text) == 0:
                split_text.append(s[i])
                      
            elif split_text[0] == s[i]:
                split_text.append(s[i])
                s_cnt += 1
            
            else:
                split_text.append(s[i])
                s_cnt -= 1   
            
        else:
            result.append("".join(split_text))
            split_text = []
            s_cnt = 1
            split_text.append(s[i])
            
    answer = len(result) + 1
    return answer