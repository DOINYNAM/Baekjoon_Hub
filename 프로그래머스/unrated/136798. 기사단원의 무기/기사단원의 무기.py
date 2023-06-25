def solution(number, limit, power):
    result = []
    
    for n in range(1, number+1):
        div_cnt = 0
        
        for i in range(1, int(n**(1/2)) + 1):
            if (n % i == 0):
                div_cnt += 1
                
                if ( (i**2) != n) : 
                    div_cnt += 1
        
        if div_cnt <= limit:
            result.append(div_cnt)
            
        else:
            result.append(power)
            
    return sum(result)