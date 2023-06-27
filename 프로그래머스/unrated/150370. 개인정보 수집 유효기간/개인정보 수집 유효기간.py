import datetime

def solution(today, terms, privacies):
    t_y, t_m, t_d = map(int, today.split("."))
    term_dic = {}
    result = []
    
    for i in terms:
        term_dic[i.split()[0]] = int(i.split()[1])
    
    for i in range(len(privacies)):
        p_date, prv = privacies[i].split()
        p_y, p_m, p_d = map(int, p_date.split("."))
        
        p_y += term_dic[prv]//12
        
        if p_m + term_dic[prv]%12 > 12:
            p_y += 1
            p_m = p_m + term_dic[prv]%12 - 12
            
        else:
            p_m = p_m + term_dic[prv]%12
            
        if t_y > p_y:
            result.append(i+1)
        
        elif t_y == p_y and t_m > p_m:
            result.append(i+1)
        
        elif t_y == p_y and t_m == p_m and t_d >= p_d:
            result.append(i+1)
        
    return result

# another
def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire