from sys import stdin
from time import time
n = stdin.readline().strip().split()
n = [int(x) for x in n]
nb_repassage = 0 
nb_Visited = 0
iterations = int(max(n))+1
nb_edge = int((iterations*(iterations-1))/2)
t = time()
graph = [0 for _ in range(nb_edge)]
print(time()-t)
t = time()
for i in range(1,len(n)):
    x1, x2 = [n[i],n[i-1]]
    if x1 != x2:
        if graph[x1+x2] == 0:
            graph[x1+x2] = 1 
            nb_Visited+=1
        else:
            graph[x1+x2] +=1
            if graph[x1+x2] == 2 :
                nb_repassage+=1
            else:
                continue
print(time()-t)
print(graph)
nb_notVisited = nb_edge-nb_Visited
if nb_repassage == 0 and nb_notVisited==0:
    print(0,0,0)
else:
    print(1,nb_notVisited,nb_repassage)

n = list(map(int,input().strip().split()))

