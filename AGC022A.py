# AGC 022 A
S = input()
T = "abcdefghijklmnopqrstuvwxyz"
A = [str(x) for x in T]

if len(S) != 26:
    for l in S:
        A.remove(l)
    print(S+A[0])
    exit()

if S == T[::-1]:
    print(-1)
    exit(0)

U = []
for k in range(1,26):
    if S[-k-1] > S[-k]:
        U.append(S[-k-1])
        U.append(S[-k])
    else:
        U.append(S[-k-1])
        U.append(S[-k])
        t = S[-k-1]
        S = S[:-k-1]
        break

U.sort()
for l in U:
    if t < l:
        print(S+l)
        exit(0)
