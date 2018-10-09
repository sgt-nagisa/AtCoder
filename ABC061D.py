# ABC 061 D
# Bellman-Ford

N, M = map(int, input().split())
INF = float("inf")

G = []
# from a to b cost c
for k in range(M):
    a, b, c = map(int, input().split())
    G.append([a-1,b-1,-c])

dist = [INF for k in range(N)]
dist[0] = 0

for k in range(N-1):
    for l in range(M):
        a, b, c = G[l][0], G[l][1], G[l][2]
        if dist[a] != INF and dist[b] > dist[a] + c:
            dist[b] = dist[a] + c

# find a negative loop
negative = [0 for k in range(N)]
for k in range(N):
    for l in range(M):
        a, b, c = G[l][0], G[l][1], G[l][2]
        if dist[a] != INF and dist[b] > dist[a] + c:
            dist[b] = dist[a] + c
            negative[b] = 1
        if negative[a] == 1:
            negative[b] = 1

print("inf" if negative[N-1] else -dist[N-1])
