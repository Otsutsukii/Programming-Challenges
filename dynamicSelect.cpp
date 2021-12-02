#include <iostream>
#include <algorithm>

using namespace std; 

struct Activitiy { 
    int start, finish; 
}; 
  

bool activityCompare(Activitiy s1, Activitiy s2) 
{ 
    return (s1.finish < s2.finish); 
} 
  
// Driver program 
void main() { 	
	ios_base::sync_with_stdio(0);
    cin.tie(0);
	int maxi=1;
	int nb;
	cin >> nb;
	Activitiy *time = new Activitiy[nb];
	for(int i=0 ; i<nb;i++){
        cin >> time[i].start >> time[i].finish;

    }
	if(nb == 0){
        cout<<0<<endl;
    }
	else{
	sort(time, time+nb, activityCompare); 
    int i = 0; 
    for (int j = 1; j < nb; j++) { 
		cout<<time[j].finish<<endl;
      if (time[j].start >= time[i].finish) { 
		  maxi++;
          i = j; 
      } 
    }
	} 
} 