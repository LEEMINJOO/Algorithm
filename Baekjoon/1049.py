import sys
q = lambda : sys.stdin.readline().strip()

N, M = map(int,q().split())

for m in range(M):
	pack, alone = map(int,q().split())
	if m == 0:
		pack_min = pack
		alone_min = alone
	else:
		if pack_min > pack:
			pack_min = pack
		if alone_min > alone:
			alone_min = alone

case_1 = (N//6 + 1) * pack_min
case_2 = N//6*pack_min + N%6*alone_min
case_3 = N*alone_min

print(min(case_1,case_2,case_3))