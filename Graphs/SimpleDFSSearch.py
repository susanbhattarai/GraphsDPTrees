graph = {'A':['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

def searchGraphDFS(graph, start, end):
    visited = set()
    dfsStack = [start]
    visited.add(start)
    while len(dfsStack) > 0:
        node = dfsStack.pop()
        if node:
            for nodes in graph[node]:
                if nodes not in visited:
                    if nodes == end:
                        return True
                    else:
                        dfsStack.append(nodes)
                        visited.add(nodes)
    return False


print searchGraphDFS(graph, "A", "F")
    
    
                        