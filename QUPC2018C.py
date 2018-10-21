# QUPC 2018 C
# BFS
from collections import deque
INF = 10**9 + 7

H, W, X = map(int,input().split())
s = [[l for l in input()] for k in range(H)]

sx, sy = 0, 0
gx, gy = 0, 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
I = deque()

for h in range(H):
    for w in range(W):
        if s[h][w] == "@":
            s[h][w] = "#"
            I.append([h,w,X])
        if s[h][w] == "G":
            gx, gy = h, w
        if s[h][w] == "S":
            sx, sy = h, w

while len(I) > 0:
    i = I.popleft()
    x, y, t = i[0], i[1], i[2]
    if t == 0:
        pass
    else:
        for k in range(4):
            if 0<=x+dx[k]<H and 0<=y+dy[k]<W:
                if s[x+dx[k]][y+dy[k]] == "G":
                    print(-1)
                    exit(0)
                if s[x+dx[k]][y+dy[k]] == ".":
                    s[x+dx[k]][y+dy[k]] = "#"
                    I.append([x+dx[k],y+dy[k],t-1])

s[gx][gy] = "."
dist = [[INF for k in range(W)] for l in range(H)]
dist[sx][sy] = 0
Q = deque()
Q.append([sx,sy])
while len(Q) > 0:
    q = Q.popleft()
    x, y = q[0], q[1]
    for k in range(4):
        if 0<=x+dx[k]<H and 0<=y+dy[k]<W:
            if s[x+dx[k]][y+dy[k]] == "." and dist[x+dx[k]][y+dy[k]] == INF:
                dist[x+dx[k]][y+dy[k]] = dist[x][y]+1
                Q.append([x+dx[k],y+dy[k]])

print(dist[gx][gy] if dist[gx][gy] != INF else -1)
