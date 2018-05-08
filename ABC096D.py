# ABC 096 D
import math

N = int(input())
P = []

for k in range(2,55555):
    f = 1
    for l in range(2,int(math.sqrt(k))+1):
        if k%l==0:
            f = 0
    if f and k%5==1:
        P.append(k)
    if len(P)>=N:
        break

print(" ".join(map(str,P)))
