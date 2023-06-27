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
            # print("case1")
            # print("t_y, p_y:", t_y, p_y)
            # print(result)
        
        elif t_y == p_y and t_m > p_m:
            result.append(i+1)
            # print("case2")
            # print("t_y, p_y:", t_y, p_y)
            # print("t_m, p_m:", t_m, p_m)
            # print(result)
        
        elif t_y == p_y and t_m == p_m and t_d >= p_d:
            result.append(i+1)
            # print("case3")
            # print("t_y, p_y:", t_y, p_y)
            # print("t_m, p_m:", t_m, p_m)
            # print("t_d, p_d:", t_d, p_d)
            # print(result)
        
    return result