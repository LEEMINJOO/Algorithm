import sys
q = lambda : sys.stdin.readline().strip()

N = int(q())
mod = 1000000
def mat_mul(A,B):
	result = []
	for i in range(2):
		row = []
		for j in range(2):
			tmp = 0
			for k in range(2):
				tmp += A[i][k] * B[k][j]
			row.append(tmp%mod)
		result.append(row)
	return result

result = [[1],[0]]
A = [[1,1],
	[1,0]]

A_mul = A[:]
for a in bin(N-1)[-1:1:-1]:
	if int(a) == 1:
		if result[1][0] == 0:
			result = A_mul
		else:
			result = mat_mul(result,A_mul)
	A_mul = mat_mul(A_mul,A_mul)

print(result[0][0]%mod)