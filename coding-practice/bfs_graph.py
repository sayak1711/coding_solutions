from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # directed graph
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def BFS(self):
        q = []
        # boolean list to mark nodes as visited or not
        # this assumes that the num on each node lies in [0, num_of_nodes]
        visited = [False]*(len(self.graph))

        ans = []
        all_visited = False
        while not all_visited:  # without this you won't cover all nodes in directed or disconnected graphs
            # for e.g if you start with 3 you'll end up with only 3
            cur_node = len(self.graph)+2
            for node, status in enumerate(visited):
                if not status:  # not visited
                    cur_node = node
                    q.append(cur_node)
                    visited[cur_node] = True
                    break
            if cur_node > len(self.graph):
                all_visited = True
            
            # now we do BFS traversal
            while q:
                cur_node = q.pop(0)
                ans.append(str(cur_node))
                for adjacent_node in self.graph[cur_node]:
                    if not visited[adjacent_node]:
                        visited[adjacent_node] = True
                        q.append(adjacent_node)
        
        print(f"BFS of graph is {'-->'.join(ans)}")

# https://media.geeksforgeeks.org/wp-content/uploads/bfs-5.png
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print(g.graph)
g.BFS()