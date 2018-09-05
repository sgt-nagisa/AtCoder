# ABC 099 D
# Other
N, C = map(int, input().split())
D = [list(map(int, input().split())) for k in range(C)]
G = [list(map(int, input().split())) for k in range(N)]

M = [[0,0,0] for k in range(C)]
for x in range(N):
    for y in range(N):
        M[G[x][y]-1][(x+y)%3] += 1

ans = 10**9
for p in range(C):
    for q in range(C):
        for r in range(C):
            if p!=q and q!=r and r!=p:
                t = 0
                for s in range(C):
                    t += D[s][p]*M[s][0]+ D[s][q]*M[s][1] + D[s][r]*M[s][2]
                ans = min(t,ans)

print(ans)