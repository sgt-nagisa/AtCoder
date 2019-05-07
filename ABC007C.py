# ABC 007 C
# BFS
from queue import Queue
INF = float("inf")

R, C = map(int,input().split())
sx, sy = map(int,input().split())
gx, gy = map(int,input().split())
M = [input() for k in range(R)]
D = [[INF for k in range(C)] for l in range(R)]

Q = Queue()
Q.put([sx-1,sy-1])

D[sx-1][sy-1] = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
while not Q.empty():
    t = Q.get()
    x = t[0]
    y = t[1]
    for k in range(4):
        if 0 <= x + dx[k] < R and 0 <= y + dy[k] < C:
            if M[x+dx[k]][y+dy[k]] == "." and D[x+dx[k]][y+dy[k]] > D[x][y]+1:
                D[x+dx[k]][y+dy[k]] = D[x][y]+1
                Q.put([x+dx[k],y+dy[k]])

print(D[gx-1][gy-1])