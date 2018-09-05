// ABC 097 D
// Union Find
#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i = 0; i < (int)(n); ++i)

int parent[100010],sequence[100010];
int N, M, x, y;

int find(int x){
    return parent[x]==x?x:parent[x]=find(parent[x]);
}
void unite(int x, int y){
    parent[find(x)] = find(y);
}

int main() {
    cin >> N >> M;
    REP(i,N){
        cin >> sequence[i];
        sequence[i]--;
        parent[i] = i;}
    REP(i,M){
        cin >> x >> y;
        x--; y--;
        unite(x,y);}
    int ans = 0;
    REP(i,N){
        if(find(i)==find(sequence[i])){
            ans++;}}
    cout << ans << endl;
    return 0;
}
