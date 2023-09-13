def solution(array, commands):
    answer = []
    
    for cmd in commands:
        list = sorted(array[cmd[0]-1 : cmd[1]])
        answer.append(list[cmd[2]-1])
    
    return answer