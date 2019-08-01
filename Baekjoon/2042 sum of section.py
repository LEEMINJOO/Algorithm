#https://www.acmicpc.net/problem/2042
import sys
q = lambda : sys.stdin.readline().strip()

def make_sum_tree(lst, depth):
	tree = [0 for _ in range(2**depth)]
	tree += lst
	pos = (len(tree)-1)//2
	if len(tree)%2 == 1 :
		tree.append(0)
	for i in reversed(range(1,pos+1)):
		tree[i] = tree[i*2]+tree[i*2+1]
	return tree

def update_tree(tree,depth,pos,new_value):
	pos = 2**depth+pos-1
	tree[pos] = new_value
	pos = pos//2
	while pos >= 1:
		tree[pos] = tree[pos*2]+tree[pos*2+1]
		pos = pos//2

def get_sum(start,end,segment_start,segment_end,now):
	if (start>segment_end) or (end<segment_start):
		return 0
	if (start<=segment_start) and (segment_end<=end):
		return tree[now]
	mid = (segment_start + segment_end)//2
	left = get_sum(start,end,segment_start,mid,now*2)
	right = get_sum(start,end,mid+1,segment_end,now*2+1)
	return left+right


N, M, K= map(int,q().split())
num_lst = [int(q()) for _ in range(N)]
depth = len(bin(N))-2

tree = make_sum_tree(num_lst,depth)

for _ in range(M+K):
	k, a, b = map(int,q().split())
	if k == 1:
		update_tree(tree,depth,a,b)
	elif k == 2:
		print(get_sum(a,b,1,2**depth,1))