
#%%
from heapq import heappop, heappush
import networkx as nx 
import numpy as np
import matplotlib.pyplot as plt

vertex_nb = 100
edges = 200
G = nx.Graph()
nodes = [i for i in range(vertex_nb)]
random_weights = list(map(int,(np.random.rand(edges)*100).tolist()))
random_edges = [(int(v[0]*edges),int(v[1]*edges),{"weight":random_weights[index]}) for index,v in enumerate(zip(np.random.rand(edges).tolist(),np.random.rand(edges).tolist()))  ]

G.add_nodes_from( nodes )
G.add_edges_from( random_edges )
G.remove_nodes_from(list(nx.isolates(G)))
G = max(nx.connected_component_subgraphs(G), key=len) # keep the large connected component 
e = [(u, v) for (u, v, d) in G.edges(data=True) ]
edges,weights = zip(*nx.get_edge_attributes(G,'weight').items())

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos,node_size= 30)
nx.draw_networkx_edges(G, pos, edgelist=edges,width=2,edge_cmap=plt.cm.rainbow,edge_color=weights)
nx.draw_networkx_labels(G, pos, font_size=3, font_family='sans-serif')  
#nx.draw(G, with_labels=True, font_weight='bold')
plt.savefig("Graph.png", format="PNG",dpi=300)
#%%
#print(G[0])
#print(max(list(G)))

#%%
def build_edit(g1,node_path):
    g1 = g1.copy()
    cost = 0
    for edit in node_path:
        if edit[0] == "e_add":
            g1.add_edge(edit[1],edit[2])
        elif edit[0] == "e_remove":
            if edit[2] in g1[edit[1]] or edit[1] in g1[edit[2]]
            g1.remove_edge(edit[1],edit[2])
        elif edit[0] == "n_add" :
            g1.add_node(edit[1])
        elif edit[0] == "n_remove":
            g1.remove_node(edit[1])
        cost+=1
    return g1,cost

def Approximate_cost(graph,finalgraph,node_path):
    g1,cost  = build_edit(graph,node_path)
    g1_nodes , g2_nodes = list(g1) , list(finalgraph)
    for node in g1_nodes:
        if node not in finalgraph:
            cost +=1 
        else:
            for neighbor in g1[node]:
                if neighbor not in finalgraph[node]:
                    cost+=1
            for neighbor in finalgraph[node]:
                if neighbor not in g1[node]:
                    cost+=1
    same_graph = True
    for node in g1:
        if node not in g2:
            same_graph = False
        for neighbor in g1[node]:
            if neighbor not in g2[node]:
                same_graph = False False
    return same_graph , cost
    
def is_complete_path(graph,finalgraph,paths):
    g1 , _ = build_edit(graph,path)
    for node in g1:
        if node not in finalgraph:
            return False
        for neighbor in g1[node]:
            if neighbor not in finalgraph[node]:
                return False
    return True

def normalize_graph(g1,g2):
    g1_nodes , g2_nodes = list(g1), list(g2)
    cost = abs(len(g1_nodes - len(g2_nodes))
    cost += set(g1_nodes) - set(g1_nodes).intersection(set(g2_nodes))
    delete_nodes = [node for node in g1_nodes if node not in g2_nodes]
    add_nodes = [node for node in g2_nodes if node not in g1_nodes]
    g1.remove_nodes_from(delete_nodes)
    g1.add_nodes_from(add_nodes)
    return g1 , cost 

def Astar_shortestPath(graph,finalgraph):
    graph, cost_nodes = normalize_graph(graph,finalgraph)  # suppose we finish edit nodes
    keys = list(graph)
    OPEN = [("e_add",keys[0],node2) for node2 in finalgraph] + [("e_remove",keys[0],node2) for node2 in finalgraph]
    while True:
        PATHmin = OPEN.pop(OPEN.index(min(OPEN,key= lambda x:len(x) + Approximate_cost(graph,finalgraph)[1])))
        if is_complete_path(PATHmin) == True :
            return PATHmin , cost_nodes+ len(PATHmin)
        else:
            tmp = set([edit[1] for edit in PATHmin])
            k = len(tmp)
            next_keys = sorted(list(tmp - tmp.intersection(set(list(graph)))))
            if k < len(list(graph)):
                for v in finalgraph:
                    OPEN.append(PATHmin.append(("e_add",next_keys[0],v)))
                    OPEN.append(PATHmin.append(("e_remove",next_keys[0],v)))
                g1 ,_ = build_edit(graph,PATHmin)
                voisins = [("e_remove",next_keys[0],node2) for node2 in list(g1[next_keys[0]])]
                PATHnew = PATHmin.append(("e_remove",next_keys[0]))
                OPEN.append(PATHnew)
            else:
                new = [("e_add",e[1],w) for w in finalgraph for e in PATHmin if len(e) ==3]
                PATHnew = PATHmin + new
                OPEN.append(PATHnew)
    return False            


#%%
def djistra(graph,source=0,destination=None):
    n = len(graph)
    for node in graph:
        for neighbor in graph[node]:
            if graph[node][neighbor]["weight"] < 0:
                return "negative edge"

    prec = {node:None for node in graph}
    black = {node:False for node in graph}
    dist = {node:float("inf") for node in graph}
    dist[source]=0
    heap = [(0,source)]
    while heap:
        dist_node, node = heappop(heap)
        if not black[node]:
            black[node] = True
            if node == destination:
                break
            for neighbor in graph[node]:
                dist_neighbor = dist_node + graph[node][neighbor]["weight"]
                if dist_neighbor < dist[neighbor]:
                    dist[neighbor] = dist_neighbor
                    prec[neighbor] = node 
                    heappush(heap, (dist_neighbor,neighbor))
    return dist, prec

source , destination = min(list(G)),max(list(G))
print("source: ",source," destination: ",destination)
dist , prec = djistra(G,source,destination)
node = destination
djistra_path = [[node,dist[node]]]
while prec[node] != None:
    node = prec[node]
    djistra_path.insert(0,[node,dist[node]])

result_path = "--->\n".join(["node:" +str(n[0]) + ", distance:"+str(n[1]) for n in djistra_path])
print(result_path)


# %%

def bellman_ford(graph,source = 0):
    n = len(graph)
    dist = {node:float('inf') for node in graph}
    prec = {node:None for node in graph}
    dist[source] = 0
    for nb_iterations in range(n):
        changed = False
        for node in graph:
            for neighbor in graph[node]:
                dist_update = dist[node] + graph[node][neighbor]["weight"]
                if dist_update < dist[neighbor]:
                    dist[neighbor] = dist_update
                    prec[neighbor] = node
                    changed = True
        if not change:
            return dist,prec,False
    return dist,prec,True


# %%

