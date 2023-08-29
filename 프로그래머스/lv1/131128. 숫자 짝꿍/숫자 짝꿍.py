def solution(X, Y):
    X = sorted(list(X))
    Y = sorted(list(Y), reverse = True)
    same_thing = []
    
    for i in range(len(X)):
        while len(Y) > 0:
            if X[i] == Y[-1]: # 반대 방향의 인덱스끼리 비교
                same_thing.append(X[i])
                Y.pop(-1)           
                break
            
            else:
                if X[i] < Y[-1]:
                    break
                
                else:
                    Y.pop(-1)
                    
    same_thing = "".join(sorted(same_thing, reverse = True))
    
    if len(same_thing) == 0:
        return "-1"
    
    elif set(same_thing) == {"0"}:  # n개의 0으로만 구성된 경우, "0"으로 출력하기 위해 조회
        return "0"
        
    else:
        return same_thing
    
# others
def solution(X, Y):
    xList = list(X.count(str(x)) for x in range(10))
    yList = list(Y.count(str(y)) for y in range(10))
    answer = ""
    
    for i in range(9, -1, -1): # 큰 수를 만들기 위해 뒤부터 범위 설정 및 시작
        answer += str(i) * min(xList[i], yList[i])

    if answer == "":
        return "-1"
    elif answer[0] == "0" and answer[len(answer) - 1] == "0":
        return "0"
    else:
        return answer