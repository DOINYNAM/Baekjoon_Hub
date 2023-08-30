def solution(numbers):
    x = set(list(i for i in range(0,10))) - set(numbers)
    
    return sum(x)