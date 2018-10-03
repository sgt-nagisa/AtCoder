# ABC 067 D
# DFS
import sys
sys.setrecursionlimit(200000)

N = int(input())
G = [[] for k in range(N+1)]
for k in range(N-1):
    a, b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

kyori1 = [100000 for k in range(N+1)]
kyori2 = [100000 for k in range(N+1)]

def dfs1(now, dist):
    for tsugi in G[now]:
        if kyori1[tsugi] == 100000:
            kyori1[tsugi] = dist + 1
            dfs1(tsugi, dist+1)

def dfs2(now, dist):
    for tsugi in G[now]:
        if kyori2[tsugi] == 100000:
            kyori2[tsugi] = dist + 1
            dfs2(tsugi, dist+1)

kyori1[1] = 0
dfs1(1,0)

kyori2[N] = 0
dfs2(N,0)

s = 0
f = 0
for k in range(1,N+1):
    if kyori1[k] <= kyori2[k]:
        f += 1
    else:
        s += 1

print("Fennec" if f > s else "Snuke")
