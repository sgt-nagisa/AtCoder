# ABC 057 D
# Math, Combinations
import math
N, A, B = map(int,input().split())
v = sorted(list(map(int,input().split())))[::-1]

def nCr(n,r):
    return (math.factorial(n)//(math.factorial(r)*math.factorial(n-r)))

a = sum(v[:A])/A
print(a)

s = 0
for k in range(N):
    if v[A-1] == v[k]:
        s += 1
t = 0
for k in range(A):
    if v[A-1] == v[k]:
        t += 1
u = 0
for k in range(A-1,B):
    if v[A-1] == v[k]:
        u += 1

if a != v[A-1]:
    print(nCr(s,t))
else:
    c = 0
    for k in range(A,A+u):
        c += nCr(s,k)
    print(c)
