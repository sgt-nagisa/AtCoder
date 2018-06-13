// AGC 019 A
#include <bits/stdc++.h>
#define REP(i,n) for(int i = 0; i < (int)(n); ++i)
#define ll long long
using namespace std;

int main(){
    ll Q, H, S, D, N;
    cin >> Q >> H >> S >> D >> N;
    cout << min({4*Q*N, (2*Q+H)*N, 2*H*N, S*N, D*(N/2)+(N%2)*min({4*Q,2*Q+H,2*H,S})}) << endl;
    return 0;
}
