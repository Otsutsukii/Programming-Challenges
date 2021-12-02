from sys import stdin
n = stdin.readline().strip().split()
n = [int(x) for x in n]
graph = {}
nb_repassage = 0 
nb_Visited = 0
iterations = int(max(n))
for i in range(iterations+1):
    for j in range(iterations+1):
        if i != j:
            mini , maxi = sorted([i,j])
            mini , maxi = str(mini) , str(maxi)
            if mini+ maxi not in graph:
                graph[mini+maxi] = 0 
for i in range(1,len(n)):
    mini , maxi = sorted([n[i],n[i-1]])
    mini , maxi = str(mini) , str(maxi)
    if mini != maxi:
        if graph[mini+maxi] == 0:
            graph[mini+maxi] = 1 
            nb_Visited+=1
        else:
            graph[mini+maxi]+=1
            if graph[mini+maxi] == 2:
                nb_repassage+=1
print(graph)
iterations +=1
nb_notVisited = int((iterations*(iterations-1))/2)-nb_Visited
if nb_repassage == 0 and nb_notVisited==0:
    print(0,0,0)
else:
    print(1,nb_notVisited,nb_repassage)


