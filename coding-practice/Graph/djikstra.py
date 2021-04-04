import sys
import heapq


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def dijkstra(self, source):
        distances = [sys.maxsize] * self.V
        distances[source] = 0
        visited = [False]*self.V
        priority_queue = []
        heapq.heappush(priority_queue, (0, source))
        while priority_queue:
            node = heapq.heappop(priority_queue)
            if visited[node[1]]:
                continue
            visited[node[1]] = True
            for v in range(self.V):
                if g.graph[node[1]][v] > 0 and not visited[v] and node[0]+g.graph[node[1]][v] < distances[v]:
                    distances[v] = node[0]+g.graph[node[1]][v]
                    heapq.heappush(priority_queue, (distances[v], v))
        print(dict(zip(range(self.V), distances)))


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
g.dijkstra(0)
