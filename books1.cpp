#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
	int n;
	cin>>n;
	while(n--){
		int m,k;
		cin>>m>>k;
		int a[502];
		int sum=0;
		for(int i=1;i<=m;i++){ 
			cin>>a[i];
			sum+=a[i];
		}
		int lo = *max_element(a+1,a+m+1);
		int hi = sum;
 
		while(lo<hi){
			int mid = lo + (hi-lo)/2;
			int s=0;
			int req=1;
			for(int i=m; i>=1 ; i--){
				if(s + a[i] <= mid){
					s += a[i];
                    cout <<"s value "<<s<<endl;
				}
				else{
					s = a[i];
					++req;
                    cout << s<<endl;
				}
			}
            cout<<"low "<<lo<<" mid "<< mid << " high " <<hi<<endl;
			if(req<=k)
				hi = mid;
			else
				lo = mid+1;
            cout<<"low "<<lo<<" mid "<< mid << " high " <<hi<<endl;
            cout <<endl;
		}
 
 
		vector<int>v;
		int placed = 1;
		int s = 0;
		for(int i=m; i>=1 ; i--){
            cout << "i-1 = "<<i-1<< " ///k-1-placed = "<<k-1-placed<<endl;
			if(s + a[i] <= lo && i-1>(k-1-placed)){
                
				s += a[i];
			}
			else{
				s = a[i];
				placed++;
				v.push_back(i);
			}
		}
 
		cout<<lo<<"   ";
		for(int i=0 ; i < v.size() ; i++)
			cout<<v[i]<<" ";
 
		// print output here
	}
}