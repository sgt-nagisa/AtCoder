# ABC091 C

from collections import Counter
N = int(input())
A = list(map(int, input().split()))

S = [0 for k in range(N)]
for k in range(N):
    S[k] = S[k-1] + A[k]

S = [0] + S
S = Counter(S)

ans = 0
for k in S:
    ans += (S[k]*(S[k]-1))//2

print(ans)
