def solution(data, ext, val_ext, sort_by):
    std_dic = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    answer = []
    
    for dt in data:
        if dt[std_dic[ext]] < val_ext:
            answer.append(dt)
            
    answer.sort(key = lambda x:x[std_dic[sort_by]])
    
    return answer