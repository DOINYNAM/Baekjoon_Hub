def solution(lottos, win_nums):
    rank_dic = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    bonus = lottos.count(0)
    
    if bonus == 6:
        return [1, 6]
    
    else:
        cnt = 0
        while len(lottos) > 0:
            if lottos[-1] in win_nums:
                cnt += 1
            lottos.pop()
    
        return [rank_dic[cnt + bonus] , rank_dic[cnt]]