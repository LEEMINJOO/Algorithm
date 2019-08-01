import sys
q = lambda : sys.stdin.readline().strip()

_ = int(q())
A = set(map(int,q().split()))
_ = int(q())
tmp_lst = list(map(int,q().split()))
for tmp in tmp_lst:
	if tmp in A:
		print('1')
	else:
		print('0')