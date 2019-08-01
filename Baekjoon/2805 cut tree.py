#https://www.acmicpc.net/problem/2805

import sys
q = lambda : sys.stdin.readline().strip()

N, M = map(int,q().split())
tree_lst = list(map(int,q().split()))

def after_cut(hight):
	after = [a-hight for a in tree_lst if a>=hight]
	return sum(after)

min_hight = 0
max_hight = max(tree_lst)

while True:
	mid = (min_hight+max_hight)//2
	if max_hight-1 <= min_hight :
		break
	if after_cut(mid) >= M:
		min_hight = mid
	else:
		max_hight = mid

print(mid)