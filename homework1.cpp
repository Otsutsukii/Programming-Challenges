/* 
student : tao zhaopeng
email : zhaopeg.tao@etu.unice.fr
master 1 EIT digital data science

Solution with complexity O(E)
I used adjancency matrix for representing the complete graph , but since the graph is unoriented 
I can optimize the matrix and use only the upper triangle part which save space memory from E*E to only E space complexity 
for representing edges.

The solution was first found with python and then optimized with c++ for speed 

*/

#include <iostream>
#include <string>
#include <vector>
#include <sstream> 
using namespace std;

int main()
{       
	/*
	reading input with competitive programming standard
	in the same time i compute the length , the max in order to avoid another iteration over the input
	
	
	*/
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    string str;
    vector<int> n;
    getline( cin, str ); 
    istringstream is( str );
    int number;
    int length = 0;
    int max=0;
    while(is>>number){
        length++;
        n.push_back(number);
        if(number>max){
            max = number;
        }
    }
    int repassage = 0;
   
    
   /*
   Create the graph for this problem , 
   it is a adjancy matrix but with upper triangle only 
   */
    max++;
    int nb_edge = (max*(max-1))/2;
    
    vector<vector<int>> graph;
    for(int i = 0; i<max;i++){
        vector<int> tmp;
        for(int j = 0 ; j<i;j++){
            tmp.push_back(0);
        }
        graph.push_back(tmp);
    }
    
       /*
   now I use the graph for solving the problem
   when a element in the matrix is 0 , I visit it given the path by the cleaner and decrease the number of edges to visit
   
   but if that edge is already visited so it must equal to 1 , the n I increament it and count a passage
   
   but since my adjacency matrix is triangular and have no lower side , I have to use it in an order with the first node 
   smaller than the second node , from the iteration order
   
   */

    for(int i=1;i<length;i++){
        if(n[i]<n[i-1]){
            if(graph[n[i-1]][n[i]] == 0){
                graph[n[i-1]][n[i]] = 1;
                nb_edge-=1;
            }
            else if (graph[n[i-1]][n[i]]==1 )
            {
                graph[n[i-1]][n[i]]++;
                repassage++;
            }}
        else{
            if (graph[n[i]][n[i-1]] == 0)
            {
                graph[n[i]][n[i-1]] = 1;
                nb_edge-=1;
            }
            else if (graph[n[i]][n[i-1]]==1)
            {
                graph[n[i]][n[i-1]]++;
                repassage++;
            }
            
            
        }
    }
    
    /*
    no error only if the guy visited all the edges and have not visited twice a corridor 
    */

    if(repassage ==0 && nb_edge == 0){
        cout<<"0 0 0"<<endl;
    }
    else{
        cout<<"1 "<<nb_edge<<" "<<repassage<<endl;
    }
}