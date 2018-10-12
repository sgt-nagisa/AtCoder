# ABC 104 C
# bit
import math
D, G = map(int, input().split())
S = [list(map(int, input().split())) for k in range(D)]

ans = float("inf")
for k in range(2**D):
    temp_score = 0
    temp_ans = 0
    r = -1
    for l in range(D):
        if int(bin(k>>l)[-1]):
            temp_score += (l+1)*100*S[l][0] + S[l][1]
            temp_ans += S[l][0]
        else:
            r = l
    if temp_score < G:
        if G-temp_score <= (r+1)*(S[r][0]-1)*100:
            temp_ans += math.ceil((G-temp_score)/((r+1)*100))
        else:
            temp_ans = float("inf")
    ans = min(ans,temp_ans)

print(ans)
