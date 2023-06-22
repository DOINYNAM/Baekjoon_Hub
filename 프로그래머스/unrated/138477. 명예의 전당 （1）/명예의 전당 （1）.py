def solution(k, score):
    answer = []
    top3 = []

    for i in range(len(score)):
        if i + 1 <= k:
            top3.append(score[i])
            answer.append(sorted(top3)[0])
            
        else:
            top3.append(score[i])
            top3 = sorted(top3)[1:]
            answer.append(top3[0])
            
    return answer