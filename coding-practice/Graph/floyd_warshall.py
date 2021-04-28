# find shortest distances between every pair of vertices in a weighted graph
# for the number of vertices in the graph do this:
# for the kth iteration
# set cell's value to be min(present_value, d[i, k]+d[k, j]) where (i, j) is the cell
INF = float('inf')

def floyd_warshall(g, n):
    for iteration in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] = min(g[i][j], g[i][iteration]+g[iteration][j])
    
    # print it
    for row in g:
        print('\t'.join([str(num) for num in row]))


"""
            10
       (0)------->(3)
        |         /|\
      5 |          |
        |          | 1
       \|/         |
       (1)------->(2)
            3           """

graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
         ]

floyd_warshall(graph, 4)