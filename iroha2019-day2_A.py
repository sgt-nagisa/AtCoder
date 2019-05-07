# LCS (Longest Common Subsequence)
# iroha2019-day2 problem A
S = input()
T = input()
N = len(S)

lcs = [[0 for k in range(N+1)] for l in range(N+1)]
# lcs[i][j] := the length of the LCS of S[:i] and T[:j]

for i in range(1,N+1):
    for j in range(1,N+1):
        if S[i-1] == T[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])

print(lcs[N][N]+1)