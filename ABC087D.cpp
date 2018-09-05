// ABC 087 D
// Depth First Search
#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i = 0; i < (int)(n); ++i)
typedef long long ll;

int INF = 1000000007;
int N, M, l, r, d;
vector<pair<int,int>> G[100001];
vector<int> x(100001,INF);

int c = 1;
void dfs(int n){
    if(!G[n].size()){
        x[n] = n;
        return;
    }
    for(auto e: G[n]){
        if(x[e.first]==INF){
            x[e.first] = x[n] + e.second;
            dfs(e.first);
        }else{
            if(x[e.first] != x[n] + e.second){
                c = 0;
                return;
            }
        }
    }
}


int main() {
    cin >> N >> M;
    REP(i,M){
        cin >> l >> r >> d;
        l--; r--;
        G[l].push_back(make_pair(r,d));
        G[r].push_back(make_pair(l,-d));
    }
    REP(i,N){
        if(x[i]==INF){
            x[i] = i;
            dfs(i);
            if(c==0){
                cout << "No" << endl;
                return 0;
            }
        }
    }
    cout << "Yes" << endl;
    return 0;
}
