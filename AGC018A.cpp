// AGC 018 A
#include <bits/stdc++.h>
#define REP(i,n) for(int i = 0; i < (int)(n); ++i)
#define ll long long
using namespace std;

ll gcd(ll a, ll b){
    if(a < b){
        swap(a,b);
    }
    if(b==0){
        return a;
    }else{
        return gcd(b, a%b);
    }
}

int main(){
    int N, K;
    cin >> N >> K;
    vector<int> A(N,0);
    REP(i,N){
        cin >> A[i];
    }
    int t = A[0];
    REP(i,N){
        t = gcd(t,A[i]);
    }
    int M = *max_element(A.begin(),A.end());
    if(K<=M && K%t==0){
        cout << "POSSIBLE" << endl;
    }else{
        cout << "IMPOSSIBLE" << endl;
    }

    return 0;
}
