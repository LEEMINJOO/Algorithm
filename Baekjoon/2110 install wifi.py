#https://www.acmicpc.net/problem/2110
import sys
q = lambda : sys.stdin.readline().strip()

N, C = map(int,q().split())
house_lst = [int(q()) for _ in range(N)]
house_lst = sorted(house_lst)

min_gap = 1
max_gap = (house_lst[N-1] - house_lst[0])//C*2

def get_house_min(gap):
	count = 1
	now = house_lst[0]
	for h in house_lst[1:]:
		if h >= now+gap:
			count += 1
			now = h
		if count > C:
			break
	return count

while True:
	mid = (min_gap+max_gap)//2
	if max_gap-1 <= min_gap:
		break
	if get_house_min(mid)>=C:
		min_gap = mid
	else :
		max_gap = mid

print(mid)