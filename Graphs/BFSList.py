class Queue:
    def __init__(self):
        self.old = []
        self.new = []
    
    def size(self):
        return len(self.old) + len(self.new)

    def enqueue(self, val):
        self.new.append(val)
    
    def shiftStack(self):
        if len(self.old) == 0:
            while len(self.new) > 0:
                self.old.append(self.new.pop())
        
    def peek(self):
        self.shiftStack()
        return self.old[-1]
    
    def dequeue(self):
        self.shiftStack()
        return self.old.pop()
    
    def empty(self):
        return self.size() == 0

graph = {'A':['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

def searchGraphBFS(graph, start):
    visited = set();
    bfsQueue  = Queue()
    visited.add(start)
    bfsQueue.enqueue(start)
    while not bfsQueue.empty():
        currentNode= bfsQueue.dequeue()
        if currentNode:
            for nodes in graph[currentNode]:
                if nodes not in visited:
                    bfsQueue.enqueue(nodes)
                    visited.add(nodes)
    return visited


print searchGraphBFS(graph, 'A')