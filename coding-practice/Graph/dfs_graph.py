from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # directed graph
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def DFS(self, node):
        self.visited[node] = True
        print(node)
        for neighbour in self.graph[node]:
            if not self.visited[neighbour]:
                self.DFS(neighbour)

    def DFSTraversal(self, nodes):
        self.visited = [False]*len(nodes)
        for node in nodes:
            if not self.visited[node]:
                self.DFS(node)

# https://media.geeksforgeeks.org/wp-content/uploads/bfs-5.png

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print(g.graph)
g.DFSTraversal(range(0, 4))