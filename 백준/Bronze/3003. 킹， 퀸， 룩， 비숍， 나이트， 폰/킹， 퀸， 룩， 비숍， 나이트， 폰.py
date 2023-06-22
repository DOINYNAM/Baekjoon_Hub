org_pc = [1, 1, 2, 2, 2, 8]
wt_pc = list(map(int, input().split()))
del_pc = []

for i in range(len(wt_pc)):
  del_pc.append(str(org_pc[i] - wt_pc[i]))

print(" ".join(del_pc))