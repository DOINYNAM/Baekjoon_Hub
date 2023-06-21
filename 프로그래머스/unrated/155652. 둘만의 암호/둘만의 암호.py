from string import ascii_lowercase as lc

def solution(s, skip, index):
    lc_dic = {i:n for n, i in enumerate(lc)}
    answer = ""
    print(lc)
    
    for i in s:
        real_index = lc_dic[i] + 1
        index_cnt = index
        
        while index_cnt:
            if real_index == 26:
                real_index = 0
                
            if lc[real_index] in skip:
                real_index += 1

            else:
                if index_cnt == 1:
                    answer += lc[real_index]
                    break
                
                else:
                    real_index += 1
                    index_cnt -= 1
                          
    return answer