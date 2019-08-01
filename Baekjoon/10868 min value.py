#https://www.acmicpc.net/problem/10868

import sys
q = lambda : sys.stdin.readline().strip()
INF = 10**9+1

def make_min_tree(lst, depth):
	tree = [INF for _ in range(2**depth)]
	tree += lst
	pos = (len(tree)-1)//2
	if len(tree)%2 == 1 :
		tree.append(INF)
	for i in reversed(range(1,pos+1)):
		tree[i] = min(tree[i*2],tree[i*2+1])
	return tree

def get_min(start,end,segment_start,segment_end,now):
	if (start>segment_end) or (end<segment_start):
		return INF
	if (start<=segment_start) and (segment_end<=end):
		return tree[now]
	mid = (segment_start + segment_end)//2
	left = get_min(start,end,segment_start,mid,now*2)
	right = get_min(start,end,mid+1,segment_end,now*2+1)
	return min(left,right)


N, M = map(int,q().split())
num_lst = [int(q()) for _ in range(N)]
depth = len(bin(N))-2

tree = make_min_tree(num_lst,depth)

for _ in range(M):
	a, b = map(int,q().split())
	print(get_min(a,b,1,2**depth,1))