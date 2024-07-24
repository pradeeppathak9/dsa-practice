# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(graph):
            if not graph:
                return None
            print(graph.val, [el.val for el in visited.keys()])
            if graph in visited:
                return visited[graph]
                
            node = Node(graph.val)
            visited[graph] = node

            for neigh in graph.neighbors:
                node.neighbors.append(visited[neigh] if neigh in visited else dfs(neigh))
            return node
        return dfs(node)
                
