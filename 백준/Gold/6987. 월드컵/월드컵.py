import sys

def possible(wins, draws, loses):
    from itertools import combinations

    matches = list(combinations(range(6), 2))
    results = [list(x) for x in zip(wins, draws, loses)]

    def dfs(match_index):
        if match_index == len(matches):
            return all(r == 0 for result in results for r in result)
        
        i, j = matches[match_index]
        # Team i wins, Team j loses
        if results[i][0] > 0 and results[j][2] > 0:
            results[i][0] -= 1
            results[j][2] -= 1
            if dfs(match_index + 1):
                return True
            results[i][0] += 1
            results[j][2] += 1

        # Draw
        if results[i][1] > 0 and results[j][1] > 0:
            results[i][1] -= 1
            results[j][1] -= 1
            if dfs(match_index + 1):
                return True
            results[i][1] += 1
            results[j][1] += 1

        # Team j wins, Team i loses
        if results[j][0] > 0 and results[i][2] > 0:
            results[j][0] -= 1
            results[i][2] -= 1
            if dfs(match_index + 1):
                return True
            results[j][0] += 1
            results[i][2] += 1

        return False

    return dfs(0)

input_data = sys.stdin.read().strip().split()
input_data = list(map(int, input_data))
assert len(input_data) == 72  # 4 sets of data, each with 18 integers

results = []
for i in range(4):
    data = input_data[i*18:(i+1)*18]
    wins = data[0:18:3]
    draws = data[1:18:3]
    loses = data[2:18:3]
    result = 1 if possible(wins, draws, loses) else 0
    results.append(result)

print(' '.join(map(str, results)))