def solution(survey, choices):
    type_list = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    score_dic = {i:0 for i in type_list}
    surv_dic = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    result = []
    
    for i in range(len(survey)):
        if choices[i] < 4:
            score_dic[survey[i][0]] += surv_dic[choices[i]]
            
        else:
            score_dic[survey[i][1]] += surv_dic[choices[i]]

    for i in range(0, len(type_list), 2):
        if score_dic[type_list[i]] < score_dic[type_list[i+1]]:
            result.append(type_list[i+1])
            
        else:
            result.append(type_list[i])
            
    answer = "".join(result)
    return answer