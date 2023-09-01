def solution(left, right):
    answer = []
    
    for i in range(left, right + 1):
        num = []
        
        for j in range(1, int(i**(1/2)) + 1):
            if i%j == 0:
                num.append(j)
                
                if i//j != j:
                    num.append(i//j)

        if len(num) % 2 == 1:
            answer.append(-i)
            
        else:
            answer.append(i)

    return sum(answer)

# others
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer