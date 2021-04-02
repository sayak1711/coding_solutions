class Graph:
 
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # list of edges as vertex1, vertex2, weight
 
    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def kruskalMST(self):
        self.graph = sorted(self.graph, key=lambda x: x[2])  # sort by weight
        results = []  # result edges
        parent = [i for i in range(self.V)]  # this list will help track the parent of node..initial all are self parents
        rank = [0 for _ in range(self.V)]  # helps decide who will be considered parent while merging
        e = 0
        i = 0
        while e < self.V-1:  # num_of_edges = 1 less than num_of_vertices
            # check if parent of vertices of current edge are different or same
            # if they are same then adding this edge will cause a cycle to form
            p1 = self.find_parent(self.graph[i][0], parent)
            p2 = self.find_parent(self.graph[i][1], parent)
            if p1 != p2:  # they don't form a cycle
                results.append(self.graph[i])
                e += 1
                self.merge(rank, parent, p1, p2)
            i += 1  # process sorted edges one by one

        min_cost = 0
        print('MST Edges')
        for edge in results:
            print(f'{edge[0]}-->{edge[1]}: {edge[2]}')
            min_cost += edge[2]
        print(f'Cost {min_cost}')

    def find_parent(self, node, parent):
        if parent[node] == node:
            return node
        return self.find_parent(parent[node], parent)

    def merge(self, rank, parent, p1, p2):
        # this function updates parent and rank to reflect the changes due to addition of edge to result
        xroot = self.find_parent(p1, parent)
        yroot = self.find_parent(p2, parent)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[yroot] < rank[xroot]:
            parent[yroot] = xroot
        else:  # if ranks are same then make one as parent and increment its rank
            parent[yroot] = xroot
            rank[xroot] += 1


g = Graph(4)
g.addEdge(0, 1, 10)  # vertex1, vertex2, weight
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.kruskalMST()
# https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/