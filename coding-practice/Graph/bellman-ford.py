# slower than dijkstra, edges are weighted, can be used to find negative weight cycles
# do n-1 iterations where n is num of vertices


class Graph:
    def __init__(self, vertices): 
        self.V = vertices # No. of vertices
        self.graph = []
  

    def addEdge(self, u, v, w): 
        self.graph.append([u, v, w])


    def bellman_ford(self, src):
        dist = [float('inf')]*self.V
        dist[src] = 0

        for _ in range(self.V-1):
            for u, v, w in self.graph:
                if u != v and dist[v] > w+dist[u]:
                    dist[v] = w+dist[u]
        
        # now one more iteration to check if cycle exists
        for u, v, w in self.graph:
            if u != v and dist[v] > w+dist[u]:
                print('Negative cycle detected!')

        # print distances from source
        print('Vertex  | Distance')
        print('-'*17)
        for i in range(self.V):
            print(f'\t{i}   |\t  {dist[i]}')
        print('-'*17)


g = Graph(5) 
g.addEdge(0, 1, -1) 
g.addEdge(0, 2, 4) 
g.addEdge(1, 2, 3) 
g.addEdge(1, 3, 2) 
g.addEdge(1, 4, 2) 
g.addEdge(3, 2, 5) 
g.addEdge(3, 1, 1) 
g.addEdge(4, 3, -3)
g.bellman_ford(0)