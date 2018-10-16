# ABC 082 D
# DP

S = input()
x, y = map(int, input().split())

a = []
t = 0
for s in S:
    if s == "F":
        t += 1
    else:
        a.append(t)
        t = 0
a.append(t)

if a == []:
    if x == y == 0:
        print("Yes")
        exit(0)
    else:
        print("No")
        exit(0)

X = [a[0]]
Y = [0]

for k in range(1,len(a)):
    if k%2 == 0:
        nx = []
        for e in X:
            nx.append(e+a[k])
            nx.append(e-a[k])
        X = list(set(nx))
    else:
        ny = []
        for e in Y:
            ny.append(e+a[k])
            ny.append(e-a[k])
        Y = list(set(ny))

print("Yes" if x in X and y in Y else "No")
