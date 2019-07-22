N ,K = map(int,input().split())

lst = []
for i in range(N):
        lst += [int(input())]
'''
lst.append(K+1)
lst = sorted(lst)
idx = lst.index(K+1)
'''
idx = N
for i, l in enumerate(lst):
	if l > K :
		idx = i
		break

total_num = 0
for i in reversed(range(idx)):
	if K == 0:
		break
	total_num += K//lst[i]
	K %= lst[i]

print(total_num)
