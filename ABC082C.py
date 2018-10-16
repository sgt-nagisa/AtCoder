# ABC 082 C
# Counter

from collections import Counter
N = int(input())
a = list(map(int,input().split()))
C = Counter(a)
ans = 0

for e in C:
    if C[e] >= e:
        ans += C[e]-e
    else:
        ans += C[e]

print(ans)
