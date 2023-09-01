def solution(left, right):
    answer = []
    for i in range(left, right + 1):
        num = []
        for j in range(1, int(i**(1/2)) + 1):
            if i%j == 0:
                num.append(j)
                num.append(i//j)

        if len(set(num)) % 2 == 1:
            answer.append(-i)
            
        else:
            answer.append(i)

    return sum(answer)

# 짝수 + / 홀수 -