import sys
import time
q = lambda : sys.stdin.readline().strip()

T = int(q())

for t in range(T):
	N = int(q())
	n_lst = range(N)
	total = 0
	t1_rank = [0 for i in n_lst]
	t2_rank = [0 for i in n_lst]
	t1_lst = []
	t2_lst = []
	for n in n_lst:
		t1, t2 = map(int,q().split())
		t1_rank[t1-1] = n
		t2_lst.append(t2-1)
	top = N
	for n in t1_rank:
		if t2_lst[n] < top:
			top = t2_lst[n]
			total += 1
	print(total)