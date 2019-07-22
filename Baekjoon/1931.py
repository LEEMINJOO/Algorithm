import sys
q = lambda : sys.stdin.readline().strip()

N = int(q())
time_dict = {}
for n in range(N):
	start, end = map(int,q().split())
	if start in time_dict:
		if time_dict[start] > end:
			time_dict[start] = end
	else:
		time_dict[start] = end

time_dict = dict(sorted(time_dict.items(), key=lambda t : t[1]))
start_lst = list(time_dict.keys())

end_time = 0
total = 0

for s in start_lst:
	if s >= end_time:
		end_time = time_dict[s]
		total += 1
'''
while True:
	start_lst_tmp = start_lst[idx:]
	for i,s in enumerate(start_lst_tmp):
		if s >= end_time:
			start_time = s
			idx = idx+i+1
			break
	if start_time not in start_lst_tmp:
		break
	end_time = time_dict[start_time]
	total += 1
'''
print(total)
