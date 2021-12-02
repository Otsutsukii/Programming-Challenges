

/* 
student : tao zhaopeng
email : zhaopeg.tao@etu.unice.fr
master 1 EIT digital data science

#2507150November 24, 2019 21:12
#2624053December 7, 2019 14:43
Solution with a time and space complexity of O(n) 
*/

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool sortbysec(const pair<int, int>& a,  
               const pair<int, int>& b) 
{ 
    return (a.second < b.second); 
} 

int main()
{       
	/*
	reading input with competitive programming standard
	in the same time i compute the length , the max in order to avoid another iteration over the input
	*/
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int nb;
    int j = 0;
    int maxi = 1;
    cin >> nb;
    vector<pair<int,int>> time(nb);
        /*
    reading input by creating a vector of pair elements start and end time 
    */
    for(int i=0 ; i<nb;i++){
        cin >> time[i].first >> time[i].second;

    }
        /*
    sort the elements by end time 
    */
    sort(time.begin(), time.end(), sortbysec);
    if(nb == 0){ // if the the the number of activity is 0 then 0 room is selected 
        cout<<0<<endl;
    }
    else{
        /*
    the variable j is the last event that we keep , so we keep just his index,
    since the vector is sorted the first i should be the first event in that room 
    and we iterate , trying to find the next event that start when the previous event finish 
    if we found then the index j become the last event we have to keep
    */
    for(int i = 1;i<nb;i++){
        if (time[i].first >= time[j].second) { 
          maxi++;
          j = i ;
          } 
        
    }
    cout<<maxi<<endl;
    }
}