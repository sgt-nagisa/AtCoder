# ABC 083 D
S = input()
t = len(S)

for k in range(1,len(S)):
    if S[k-1] != S[k]:
        t = min(t, max(k,len(S)-k))

print(t)
