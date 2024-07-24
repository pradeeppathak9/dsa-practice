# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(graph):
            if not graph:
                return None
            if graph in visited:
                return visited[graph]
                
            node = Node(graph.val)
            visited[graph] = node

            for neigh in graph.neighbors:
                node.neighbors.append(visited[neigh] if neigh in visited else dfs(neigh))
            return node
        return dfs(node)


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def bfs(graph):
            if graph:
                queue  = deque()
                visited = {}
                queue.append(graph)
                node = Node(graph.val)
                visited[graph] = node

                while queue:
                    src = queue.popleft()
                    for neigh in src.neighbors:
                        if neigh not in visited: 
                            node = Node(neigh.val)
                            visited[neigh] = node
                            queue.append(neigh)
                        visited[src].neighbors.append(visited[neigh])
                return visited[graph]
        return bfs(node)




# local implementation
class Node:
    val = None
    neighbors = []
    
    def __init__(self, val):
        self.val = val

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node1.neighbors = [node2, node3]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node1]

    print([ el.val for el in node1.neighbors ] )
    print([ el.val for el in node2.neighbors ] )
    print([ el.val for el in node3.neighbors ] )

    visited = {}
    def dfs(graph):
        if not graph:
            return None
        if graph in visited:
            return visited[graph]
            
        node = Node(graph.val)
        visited[graph] = node
    
        for neigh in graph.neighbors:
            node.neighbors.append(visited[neigh] if neigh in visited else dfs(neigh))
        return node
        
    clonded_graph = dfs(node1)


                
                
