// ABC 070 D
// Dijkstra
#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i = 0; i < (int)(n); ++i)
typedef long long ll;

// DIJKSTRA
// cf. arihon p.96
const ll INF = 1e+18;
struct edge {int to, cost;};
vector<vector<edge>> graph(100010);
vector<ll> dist(100010, INF);
typedef pair<int,int> P; // <kyori, chouten>
void dijkstra(int s){
    priority_queue<P, vector<P>, greater<P> > Q;
    Q.push(P(0,s));
    dist[s] = 0;
    while(!Q.empty()){
        P p = Q.top(); Q.pop();  // p <kyori, chouten>
        int v = p.second;
        if(dist[v] < p.first) continue;
        for (edge e : graph[v]){
            if (dist[e.to] > dist[v] + e.cost){
                dist[e.to] = dist[v] + e.cost;
                Q.push(P(dist[e.to], e.to));
            }
        }
    }
}

int main() {
    int N, a, b, c, Q, K, x, y;
    cin >> N;
    REP(i,N-1){
        cin >> a >> b >> c;
        a--; b--;
        graph[a].push_back({b,c});
        graph[b].push_back({a,c});
    }
    cin >> Q >> K;
    K--;
    dijkstra(K);
    ll ans[Q];
    REP(i,Q){
        cin >> x >> y;
        x--; y--;
        ans[i] = dist[x] + dist[y];
    }
    REP(i,Q){
        cout << ans[i] << endl;
    }
    return 0;
}
