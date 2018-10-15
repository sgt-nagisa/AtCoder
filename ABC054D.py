# ABC 054 D
# DP
N, Ma, Mb = map(int, input().split())
P = [list(map(int, input().split())) for k in range(N)]
INF = 10000
dp = [[[INF for m in range(401)] for k in range(401)] for l in range(N+1)]
# dp[i番目までで][Aの重さ][Bの重さ]の最小コスト
dp[0][0][0] = 0

for k in range(N):
    a = P[k][0]
    b = P[k][1]
    c = P[k][2]
    for l in range(401):
        for m in range(401):
            if dp[k][l][m] != INF:
                dp[k+1][l][m] = min(dp[k+1][l][m],dp[k][l][m])
                dp[k+1][l+a][m+b] = min(dp[k+1][l+a][m+b], dp[k][l][m]+c) 

ans = INF
for l in range(1,401):
    for m in range(1,401):
        if Ma*m == Mb*l:
            ans = min(ans,dp[N][l][m])

print(ans if ans != INF else -1)