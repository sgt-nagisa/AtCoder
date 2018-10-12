# ABC 060 D
# Brute-force
N, W = map(int,input().split())
L = [list(map(int,input().split())) for k in range(N)]

wmin = L[0][0]
M = [[],[],[],[]]
for load in L:
    M[load[0]-wmin].append(load[1])

M0 = sorted(M[0])[::-1]
M1 = sorted(M[1])[::-1]
M2 = sorted(M[2])[::-1]
M3 = sorted(M[3])[::-1]

ans = 0
for p in range(len(M0)+1):
    for q in range(len(M1)+1):
        for r in range(len(M2)+1):
            for s in range(len(M3)+1):
                weight = p*wmin + q*(wmin+1) + r*(wmin+2) + s*(wmin+3)
                if weight <= W:
                    ans = max(ans,sum(M0[:p])+sum(M1[:q])+sum(M2[:r])+sum(M3[:s]))
print(ans)