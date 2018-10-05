# ABC 063 D
# bisect
from math import ceil
N, A, B = map(int,input().split())
h = []
for k in range(N):
    h.append(int(input()))

def check(t):
    s = t
    for k in range(N):
        if h[k] > B*t:
            s -= ceil((h[k]-B*t)/(A-B))
        if s < 0:
            return False
    return True

lo = 0
hi = max(h)+1

while hi - lo > 1:
    mid = (hi+lo)//2
    if check(mid):
        hi = mid
    else:
        lo = mid

print(hi)