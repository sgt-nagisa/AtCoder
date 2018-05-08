# ABC 091 C

N = int(input())
R = [list(map(int,input().split())) for k in range(N)]
B = [list(map(int,input().split())) for k in range(N)]

R = sorted(R, key = lambda x: -1*x[1])
B = sorted(B)

ans = 0
for b in B:
    for r in R:
        if r[0] < b[0] and r[1] < b[1]:
            ans += 1
            R.remove(r)
            break

print(ans)