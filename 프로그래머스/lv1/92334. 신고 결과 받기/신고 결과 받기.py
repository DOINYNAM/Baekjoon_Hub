def solution(id_list, report, k):
    mail_id_dic = {id:0 for id in id_list}
    report_id_dic = {id:[] for id in id_list}
    
    for i in report: # id별 받은 신고 수 체크
        x, y = i.split(" ")
        report_id_dic[y].append(x) # 중복 제거 필요
    
    for i in id_list: 
        report_id_dic[i] = list(set(report_id_dic[i])) # 신고자 id 중복 제거 후
        
        if len(report_id_dic[i]) >= k: # 정지 대상인지 구분
            for j in report_id_dic[i]: # 정지 대상일 때, 신고자가 받을 메일 수에 count
                mail_id_dic[j] += 1
    
    return list(mail_id_dic.values())