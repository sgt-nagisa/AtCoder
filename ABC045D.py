# ABC 045 D
# Counter
from collections import Counter
H, W, N = map(int, input().split())
L = []
for k in range(N):
    a, b = map(int, input().split())
    for k in range(3):
        for l in range(3):
            if 1 <= a-k <= H-2  and 1 <= b-l <= W-2:
                L.append((a-k,b-l))

M = Counter(L)
A = [0 for k in range(10)]
s = 0
for e in M:
    A[M[e]] += 1
    s += 1

A[0] = (H-2)*(W-2)-s
for a in A:
    print(a)
