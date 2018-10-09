# ABC 110 D
# Math
import math, collections
N, M = map(int,input().split())
MOD = 7+10**9

if M == 1:
    print(1)
    exit(0)

# prime factorization
Q = []
k = 2
while k < M:
    if M%k == 0:
        Q.append(k)
        M //= k
    else:
        k += 1
Q.append(k)

R = collections.Counter(Q)

def nCr(n,r):
    return (math.factorial(n)//(math.factorial(r)*math.factorial(n-r)))%MOD

ans = 1
for f in R:
    ans *= nCr(N+R[f]-1,R[f])
    ans %= MOD
print(ans)
