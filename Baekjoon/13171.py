import sys
import math
q = lambda : sys.stdin.readline().strip()

A = int(q())
X = int(q())
A = A%(10**9+7)
i = 0
result = 1
mul_list = [A]

while True :
	if X%2 == 1 :
		result *= mul_list[i]
	X = X//2
	if X == 0 :
		break
	mul_list += [(mul_list[i]**2)%(10**9+7)]
	i += 1
print(result%(10**9+7))

'''
for i in range(int(math.log2(X)),-1,-1):
    print(X)
    now = 2**i
    # 2진법의 결과
    exist = X//now
    X = X%now
    if exist == 1 :
            result *= (A**now)
    if X == 0 :
            break
print(result%(10**9+7))'''
