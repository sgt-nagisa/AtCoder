# ABC 064 D
N = int(input())
S = input()
R = S[::-1]

if S.count(")") == 0:
    print(S+")"*N)
    exit(0)
elif S.count("(") == 0:
    print("("*N+S)
    exit(0)

f = R.index(")")
g = S.index("(")

t = [0 for k in range(N)]
l = 0
for k in range(N-f):
    if S[k] == ")":
        l += 1
    else:
        l -= 1
    t[k] = l

s = [0 for k in range(N)]
m = 0
for k in range(len(S)-g):
    if S[-1-k] == "(":
        m += 1
    else:
        m -= 1
    s[k] = m

print("("*max(t)+S+")"*max(s))
