# topologically sort a graph
# elements in a DAG with higher precedence(lesser indegrees) will come first. used to find dependencies.
from collections import defaultdict, deque
from textwrap import indent

class TopologicalSort:
    def __init__(self, nodes):
        self.graph = defaultdict(list)  # directed graph
        self.indegrees = defaultdict(lambda: 0)
        self.nodes = nodes

    def addEdges(self, edges):
        for edge in edges:
           self.graph[edge[0]].append(edge[1])
           self.indegrees[edge[1]] += 1
    
    def tsort_dfs(self):
        st = []
        self.visited = defaultdict(lambda: False)
        for node in self.nodes:
            if not self.visited[node]:
                self.dfs(node, st)
        print(st[::-1])

    def dfs(self, node, st):
        self.visited[node] = True
        for nei in self.graph[node]:
            if not self.visited[nei]:
                self.dfs(nei, st)
        st.append(node)

    def tsort_bfs(self):
        q = deque()
        for node in self.nodes:
            if self.indegrees[node] == 0:
                q.append(node)
        
        while q:
            cur = q.popleft()
            print(cur)
            for nei in self.graph[cur]:
                self.indegrees[nei] -= 1
                if self.indegrees[nei] == 0:
                    q.append(nei)

g = TopologicalSort([0, 1, 2, 3, 4, 5])
g.addEdges([(5, 0), (4, 0), (5, 2), (4, 1), (2, 3), (3, 1)])
g.tsort_bfs()
print('-'*90)
g.tsort_dfs()