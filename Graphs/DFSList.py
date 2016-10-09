graph = {'A':['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

def searchGraphDFS(graph, start, end):
    visited = set()
    dfsStack = [(start, [start])]
    visited.add(start)
    while len(dfsStack) > 0:
        node, path = dfsStack.pop()
        if node:
            for nodes in graph[node]:
                if nodes not in visited:
                    if nodes == end:
                        print path + [nodes]
                    else:
                        dfsStack.append((nodes, path + [nodes]))
                        visited.add(nodes)
    return 

print searchGraphDFS(graph, "A", "F")
    
    
                        