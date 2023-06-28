def solution(k, m, score):
    score = sorted(score, reverse = True)
    m_cnt = m
    result = 0
    in_box = []
    
    for i in score:
        if m_cnt == 1:
            in_box.append(i)
            result += in_box[-1] * m
            m_cnt = m
            in_box = []
        
        else:
            in_box.append(i)
            m_cnt -= 1

    return result