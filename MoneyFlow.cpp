#include <iostream>
//#include <algorithm>
#include <vector>

using namespace std;


int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    for(int testcase = 1;;testcase++){
        int NB;
        scanf("%d", &NB);
        if(NB == 0){
            return 0 ;
        }
        int before = 0 ;
        vector<int> after(NB);
        for(int i = 0 ; i<NB;i++){
            for(int j = 0 ; j < NB;j++){
                int x; scanf("%d",&x);
                after[i]+=x;
                after[j]-=x;
                before +=x;
            }
        }
        int res=0;
        for(int i = 0 ; i < NB ; i++){
            if(after[i] > 0 ){
                res+=after[i];
            }
        }
        cout << testcase<<". "<<before<< " "<<res << endl;
    }
}