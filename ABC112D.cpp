// ABC 112 D
// Math
#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    for (int i = M/N; i > 0; --i){
        if (M%i == 0){
            cout << i << endl;
            exit(0);
        }
    }
    return 0;
}
