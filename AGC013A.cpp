// AGC 013 A
#include <bits/stdc++.h>
#define REP(i,n) for(int i = 0; i < (int)(n); ++i)
#define ll long long
using namespace std;

int main(){
    int N;
    cin >> N;
    vector<int> A(N,0);
    REP(i,N){
        cin >> A[i];}
    int s = 0;
    int ans = 1;
    REP(i,N-1){
        if(s==0){
            if (A[i]<A[i+1]){
                s = 1;
            }else if (A[i]>A[i+1]){
                s = -1;}}
        if(s==1){
            if(A[i]>A[i+1]){
                ans++;
                s = 0;}}
        if(s==-1){
            if(A[i]<A[i+1]){
                ans++;
                s = 0;}}}
    cout << ans << endl;
    return 0;
}
