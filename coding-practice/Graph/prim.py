import heapq

class Graph:
    def __init__(self, V):
        self.V = V  # number of vertices
        self.graph = [] # each index has its list of neighbors as (weight, node)

    def prim(self, start_node):
        mincost = 0
        priority_queue = []
        marked = [False]*self.V

        heapq.heappush(priority_queue, (0, start_node))  # push first node with 0 cost
        while priority_queue:
            node = heapq.heappop(priority_queue) # pop node with least cost
            if marked[node[1]]:
                continue
            marked[node[1]] = True
            mincost += node[0]
            for neighbor in self.graph[node[1]]:
                if not marked[neighbor[1]]:
                    heapq.heappush(priority_queue, neighbor)
        return mincost

# https://www.geeksforgeeks.org/wp-content/uploads/Fig-11.jpg
g = Graph(9)
g.graph = [[(4, 1), (8, 7)], [(4, 0), (8, 2), (11, 7)], [(8, 1), (2, 8), (4, 5), (7, 3)], [(7, 2), (14, 5), (9, 4)], [(9, 3), (10, 5)], [(4, 2), (14, 3), (10, 4), (2, 6)], [(2, 5), (1, 7), (6, 8)], [(8, 0), (7, 8), (1, 6), (11, 1)], [(2, 2), (6, 6), (7, 7)]]
print(g.prim(0))
# ans should be sum of edges on this figure https://www.geeksforgeeks.org/wp-content/uploads/MST5.jpg

# start with arbritary node and mark it. as it is greedy algo it will look for the 
# least weight edge among this node's neighbors and choose that neighbor and mark it
# in this manner each time we consider all edges that don't create cycle(don't have marked
# nodes on both ends) and have one end node as marked (because it has to add to the already
# existing tree)and choose minimum weight among them