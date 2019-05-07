// ABC 120 D
// Union-Find
#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i = 0; i < (int)(n); ++i)
typedef long long ll;

vector<ll> parent(100010,-1);
ll N, M, x, y;

ll find(ll x){
    return parent[x]<0?x:parent[x]=find(parent[x]);
}
void unite(ll x, ll y){
    x = find(x), y = find(y);
    if(x != y){
        if (parent[x] > parent[y]) swap(x,y);
        parent[x] += parent[y];
        parent[y] = x;
    }
}
ll size(ll x){
    return -parent[find(x)];
}

int main() {
    ll A[100010], B[100010];
    cin >> N >> M;
    REP(i,M){
        cin >> A[i] >> B[i];
        A[i]--; B[i]--;

    vector<ll> ans;
    ll t = (N*(N-1))/2;
    REP(i,M){
        ans.push_back(t);
        ll x = A[M-i-1], y = B[M-i-1];
        if(find(x)!=find(y)){
            t -= size(x)*size(y);
            unite(x,y);
        }
    }
    reverse(ans.begin(),ans.end());
    for (auto& it: ans){cout << it << endl;}
    return 0;
}
