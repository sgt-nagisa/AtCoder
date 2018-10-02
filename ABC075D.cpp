// ABC 075 D
// Brute Force
#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i = 0; i < (int)(n); ++i)
typedef long long ll;

int main() {
    int N, K, x, y;
    cin >> N >> K;
    vector<pair<int,int>> G;
    REP(i,N){
        cin >> x >> y;
        G.push_back(make_pair(x,y));
    }
    ll ans = 4e18+1;
    REP(p,N){
        REP(q,N){
            REP(r,N){
                REP(s,N){
                    ll ue = max(G[p].second,G[q].second);
                    ll shita = min(G[p].second,G[q].second);
                    ll hidari = min(G[r].first,G[s].first);
                    ll migi = max(G[r].first,G[s].first);
                    int t = 0;
                    REP(k,N){
                        if ((G[k].second<=ue)&&(shita<=G[k].second)&&(G[k].first<=migi)&&(hidari<=G[k].first)) t++;
                    }
                    if (t>=K){
                        ans = min(ans,(ue-shita)*(migi-hidari));
                    }
                }
            }
        }
    }
    cout << ans << endl;
    return 0;
}
