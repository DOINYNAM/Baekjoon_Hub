from itertools import combinations

def solution(number):
    answer = 0
    
    for n in combinations(number, 3):
        # print(n)
        
        if 0 == sum(n):
            answer += 1
            
    return answer
    
    
        