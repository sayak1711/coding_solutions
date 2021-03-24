# topologically sort a graph
# elements with higher precedence(lesser indegrees) will come first
from collections import defaultdict

class TopologicalSort:
    def __init__(self, V):
        self.graph = defaultdict(list)  # directed graph
        self.V = V  # number of vertices

    def addEdges(self, edges):
        for edge in edges:
           self.graph[edge[0]].append(edge[1])

    def kahn_tsort(self):
        # find all indegress
        indegrees = [0]*self.V
        for node in self.graph:
            for neighbor in self.graph[node]:
                indegrees[neighbor] += 1
        
        q = []  # a queue
        for node, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(node)
        
        ct = 0
        topo = []  # the sort
        while q:
            node = q.pop(0)
            topo.append(node)
            for neighbor in self.graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    q.append(neighbor)
            ct += 1
        if ct == self.V:
            print(topo)
        else:
            print('Cycle present in graph')

g = TopologicalSort(6)
g.addEdges([(5, 0), (4, 0), (5, 2), (4, 1), (2, 3), (3, 1)])
g.visited = [False]*len(range(0, 6))
g.kahn_tsort()

# time O(V+E) V: num of vertices E: num of edges
# space O(V)