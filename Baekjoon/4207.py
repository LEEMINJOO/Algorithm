import sys
q = lambda :sys.stdin.readline().strip()

def find_min_time(total,lst,N):
	lst = lst + [total//2]
	lst = sorted(lst)
	idx = lst.index(total//2)
	if idx == 0:
		return total - lst[idx+1]
	elif idx == N:
		return lst[idx-1]
	return max(lst[idx-1], total - lst[idx+1])

def find_max_time(total,lst,N):
	lst = sorted(lst)
	return max(lst[N-1],total-lst[0])

T = int(q())
result = []

for t in range(T):
	total_l, n = map(int,q().split())
	lst = []
	for i in range(n):
		lst.append(int(q()))

	print(find_min_time(total_l,lst,n), find_max_time(total_l,lst,n))