# AGC 028 A
# Math
N, M = map(int, input().split())
S = input()
T = input()

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
def lcm(a,b):
    return a*b//gcd(a,b)

if S[0] != T[0]:
    print(-1)
    exit(0)
if S == T:
    print(N)
    exit(0)

L = lcm(N,M)
p = L//N
q = L//M
U = ""
k = 0

if gcd(M,N) > 1:
    for k in range(1,L):
        if k%p == 0 and k%q == 0:
            if S[k//p] != T[k//q]:
                print(-1)
                exit(0)
    print(L)
else:
    print(L)
