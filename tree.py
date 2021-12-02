import sys

def main():
    root = 0
    data = [d.rstrip() for d in sys.stdin.readlines()]
    n,m = data[0].split()
    data = data[1:]
    graph = {}
    for i in range(int(m)):
        a,b = [x.rstrip() for x in data[i].split()]
        if a in graph:
            graph[a]['adj'].append(b)
        else:
            graph[a]={'adj':[]}
            graph[a]['adj'].append(b)
        if b not in graph:
            graph[b]={'adj':[]}
            
        if not root:
            root=a
    visited = [1 for i in range(int(n))]
    print(graph)
    stack = [root]
    while stack:
        x = stack.pop()
        print(stack)
        if visited[int(x)-1] == 0:
            print("NO")
            return 0
        elif visited[int(x)-1] == 1 :
            stack.extend(graph[x]['adj'])
            visited[int(x)-1]=0

    if sum(visited) == 0 :
        print("YES")
    else:
        print("NO")

main()