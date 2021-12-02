n = list(map(int,input().strip().split()))
nb_repassage = 0
iterations = max(n) + 1 
nb_edges = int((iterations*(iterations-1))/2)
graph = [[0 for _ in range(i)] for i in range(iterations)]


for i in range(1,len(n)):
    if n[i] < n[i-1]:
        if graph[n[i-1]][n[i]] == 0:
            graph[n[i-1]][n[i]] = 1 
            nb_edges-=1
        elif graph[n[i-1]][n[i]]==1 :
            graph[n[i-1]][n[i]] +=1
            nb_repassage+=1
    else:
        if graph[n[i]][n[i-1]] == 0:
            graph[n[i]][n[i-1]] = 1 
            nb_edges-=1
        elif graph[n[i]][n[i-1]]==1 :
            graph[n[i]][n[i-1]] +=1
            nb_repassage+=1 

if nb_repassage == 0 and nb_edges==0:
    print(0,0,0)
else:
    print(1,nb_edges,nb_repassage)