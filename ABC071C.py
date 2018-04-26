# ABC 071 C

from collections import Counter
N = int(input())
A = list(map(int, input().split()))
B = Counter(A)
 
c = 0
t = 0
 
for k in B:
    if k*k > c*t and B[k] >= 4:
        c = k
        t = k
    elif c >= k > t and B[k] >= 2:
        t = k
    elif k > c and B[k] >= 2:
        t = c
        c = k

print(t*c)