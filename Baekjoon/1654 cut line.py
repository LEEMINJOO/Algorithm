import sys
q = lambda : sys.stdin.readline().strip()

K, N = map(int,q().split())
line_lst = [int(q()) for _ in range(K)]

total = sum(line_lst)
result_max = total//N*2
result_min = 0

def get_total_num(line_lst, result):
	return sum([l//result for l in line_lst])

while True:
	result = (result_max + result_min)//2
	total = get_total_num(line_lst,result)
	if result_max-1 <= result_min :
		break
	if total >= N:
		result_min = result
	else :
		result_max = result
print(result_min)

