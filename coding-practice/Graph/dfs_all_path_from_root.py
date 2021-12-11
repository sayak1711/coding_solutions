class Solution:
    def allPathsSource(self, graph):
        def dfs(node, path):
            path.append(node)
            if node == len(graph) - 1:
                paths.append(path.copy())
                return

            for next_node in graph[node]:
                dfs(next_node, path)
                path.pop()

        paths = []

        if not graph or len(graph) == 0:
            return paths
        dfs(0, [])
        return paths

graph = [[4,3,1],[3,2,4],[3],[4],[]]
sol = Solution()
print(sol.allPathsSource(graph))