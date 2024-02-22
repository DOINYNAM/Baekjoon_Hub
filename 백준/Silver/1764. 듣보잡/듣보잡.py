import sys
input = sys.stdin.readline

N, M = map(int, input().split())

no_heard = [input().rstrip() for _ in range(N)]
no_seen = [input().rstrip() for _ in range(M)]

intersection = sorted(list(set(no_heard) & (set(no_seen))))

print(len(intersection))

for i in intersection:
	print(i)