# KUPC 2018 D
# DFS

H, W = map(int,input().split())
c = [input() for k in range(H)]
c = c[::-1]

def dfs(x,y,t):
    if y == H-1:
        print(t)
        exit(0)
    if 0<=x<W and 0<=y<H and c[y+1][x] == ".":
        dfs(x,y+1,t+"S")
    if 0<=x-1<W and 0<=y<H and c[y+1][x-1] == ".":
        dfs(x-1,y+1,t+"L")
    if 0<=x+1<W and 0<=y<H and c[y+1][x+1] == ".":
        dfs(x+1,y+1,t+"R")

dfs(c[0].index("s"),0,"")
print("impossible")