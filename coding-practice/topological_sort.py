# topologically sort a graph
# elements with higher precedence(lesser indegrees) will come first
from collections import defaultdict

class TopologicalSort:
    def __init__(self):
        self.graph = defaultdict(list)  # directed graph
    
    def addEdges(self, edges):
        for edge in edges:
           self.graph[edge[0]].append(edge[1])
    
    def tsort_recursive(self, st, node):
        for neighbour in self.graph[node]:
            if not self.visited[neighbour]:
                self.visited[neighbour] = True
                self.tsort_recursive(st, neighbour)
        st.append(node)

    def tsort(self, nodes):
        st = []
        for node in nodes:
            if not self.visited[node]:
                self.visited[node] = True
                self.tsort_recursive(st, node)
        for node in st[::-1]:
            print(node)

g = TopologicalSort()
g.addEdges([(5, 0), (4, 0), (5, 2), (4, 1), (2, 3), (3, 1)])
g.visited = [False]*len(range(0, 6))
g.tsort(range(0, 6))