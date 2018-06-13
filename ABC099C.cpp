// ABC 099 C
#include <bits/stdc++.h>
#define REP(i,n) for(int i = 0; i < (int)(n); ++i)
#define ll long long
using namespace std;

int main(){
    int N;
    cin >> N;
    vector<ll> dp(100001,100001);
    dp[0] = 0;
    REP(i,N+1){
        int p = 1;
        while(p<=i&&p<=N){
            dp[i] = min(dp[i],dp[i-p]+1);
            p*=6;}}
    REP(i,N+1){
        int p = 1;
        while(p<=i&&p<=N){
            dp[i] = min(dp[i],dp[i-p]+1);
            p*=9;}}
    cout << dp[N] << endl;
    return 0;
}
