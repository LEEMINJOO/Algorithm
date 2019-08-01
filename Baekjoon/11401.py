import sys
q = lambda : sys.stdin.readline().strip()
mod = 10**9 +7

N ,K = map(int,q().split())
K = N-K if K > N-K else K

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

son = 1
mom = 1
for i in range(1,K+1):
	son *= (N-i+1)
	mom *= i
	son %= mod
	mom %= mod
mom_i = get_mod_inv(mod,mom)
print(son*mom_i%mod)