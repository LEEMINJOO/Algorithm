import sys
q = lambda : sys.stdin.readline().strip()

def mat_mul(A,B,N):
	result = []
	for i in range(N):
		row_tmp = []
		for j in range(N):
			tmp = 0
			for k in range(N):
				tmp += A[i][k]*B[k][j]
			tmp %= 1000
			row_tmp += [tmp]
		result.append(row_tmp)
	return result

N, B = map(int,q().split())
A = []
for i in range(N):
	A.append(list(map(int,q().split())))

result = 1
A_mul = A[:]
for a in bin(B)[-1:1:-1]:
	if int(a) == 1:
		if result == 1:
			result = A_mul
		else:
			result = mat_mul(result,A_mul,N)
	A_mul = mat_mul(A_mul,A_mul,N)

for row in result:
	for r in row:
		print(r%1000,end=' ')
	print()
