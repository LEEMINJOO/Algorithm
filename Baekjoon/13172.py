import sys
q = lambda : sys.stdin.readline().strip()
mod = 10**9 + 7

def get_mod_inv(mod,N):
	# N ** (mod-2)
	now = N
	ans = 1
	for i,a in enumerate(bin(mod-2)[-1:1:-1]):
		if int(a) == 1:
			ans *= now
		now *= now
		now %= mod
		ans %= mod
	return ans

M = int(q())
for m in range(M):
	N, S = map(int,q().split())
	if m == 0:
		son = S
		mom = N
	else:
		son = mom*S + son*N
		mom = mom*N
	son %= mod
	mom %= mod
mom_i = get_mod_inv(mod,mom)
result = son * mom_i % mod
result %= mod
print(result)