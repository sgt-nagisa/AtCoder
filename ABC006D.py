# ABC 006 D
from bisect import bisect_left
N = int(input())
A = [int(input()) for k in range(N)]

# Longest Increasing Subsequence
INF = float("inf")
L = [INF for k in range(N+2)]
L[0] = -INF

for k in range(N):
    t = bisect_left(L,A[k])
    L[t] = A[k]

for k in range(1,N+2):
    if L[k] == INF:
        print(N-k+1)
        exit(0)
