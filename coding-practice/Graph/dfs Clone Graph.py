# Question: Clone Graph: https://leetcode.com/problems/clone-graph/

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



class DFS:
    def __init__(self):
        self.nodes = {} # one entry for each node we have recreated, so that we don't recurse for it again
    
    def traverse(self, node_val, neighbors):
        cur_node = Node(node_val)  # recreating the node using only value, neighbors will get filed in eventually
        self.nodes[node_val] = cur_node  # make an entry for it beforehand to avoid recursing indefinitely
        
        for neighbor in neighbors:
            if neighbor.val in self.nodes:  # no need to recurse for it if we already have recreated it
                neighbor_node = self.nodes[neighbor.val]
            else:
                neighbor_node = self.traverse(neighbor.val, neighbor.neighbors)
            cur_node.neighbors.append(neighbor_node)
        
        return cur_node
    
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        dfs_obj = DFS()
        root = dfs_obj.traverse(node.val, node.neighbors)
        return root