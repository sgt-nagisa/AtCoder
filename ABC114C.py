# ABC 114 C
import itertools, bisect
N = int(input())
d = len(str(N))

L =  []
for k in range(3,d+1):
    for a in itertools.product(["3","5","7"], repeat=k):
        if "3" in a and "5" in a and "7" in a:
            L.append(int("".join(a)))

L = sorted(L)
print(bisect.bisect_right(L,N))
