// AGC 017 A
#include <bits/stdc++.h>
#define REP(i,n) for(int i = 0; i < (int)(n); ++i)
#define ll long long
using namespace std;

int main(){
    int N, P;
    cin >> N >> P;
    vector<int> A(N,0);
    REP(i,N){
        cin >> A[i];}
    int c = 0;
    REP(i,N){
        if(A[i]%2==1){
            c = 1;
            break;}}
    ll ans = 0;
    if(c){
        ans = pow(2,N-1);
    }else{
        if(!P){
            ans = pow(2,N);}}
    cout << ans << endl;
    return 0;
}
