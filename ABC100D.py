# ABC 100 D
# Other
N, M = map(int, input().split())
A = [list(map(int, input().split())) for k in range(N)]

B = sum((sorted([e[0]+e[1]+e[2] for e in A])[::-1])[:M])
C = sum((sorted([e[0]-e[1]+e[2] for e in A])[::-1])[:M])
D = sum((sorted([e[0]+e[1]-e[2] for e in A])[::-1])[:M])
E = sum((sorted([0-e[0]+e[1]+e[2] for e in A])[::-1])[:M])
F = sum((sorted([e[0]-e[1]-e[2] for e in A])[::-1])[:M])
G = sum((sorted([0-e[0]-e[1]+e[2] for e in A])[::-1])[:M])
H = sum((sorted([0-e[0]+e[1]-e[2] for e in A])[::-1])[:M])
I = sum((sorted([0-e[0]-e[1]-e[2] for e in A])[::-1])[:M])

print(max(B,C,D,E,F,G,H,I))