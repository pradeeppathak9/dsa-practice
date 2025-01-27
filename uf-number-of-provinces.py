# https://leetcode.com/problems/number-of-provinces/


# union find solution 
class UnionFind(object):
    def __init__(self, parents, rank):
        self.parents = parents
        self.rank = rank

    def find(self, node):
        parent = node
        while parent != self.parents[parent]:
            # this is just a path compression
            self.parents[parent] = self.parents[self.parents[parent]]
            parent = self.parents[parent]
        return parent

    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        if p1 == p2: 
            return 0
        
        if self.rank[p1] > self.rank[p2]:
            self.parents[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parents[p1] = p2
            self.rank[p2] += self.rank[p1]
        return 1
    

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parents = [node for node in range(len(isConnected))]
        rank = [1] * len(parents)
        
        uf = UnionFind(parents=parents, rank=rank)
        result = len(parents)

        for c1 in range(len(isConnected)):
            for c2 in range(len(isConnected)):
                if isConnected[c1][c2] == 1:
                    result -= uf.union(c1, c2)
        return result   





# DFS solution 
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    adj[i].append(j)
                    adj[j].append(i)
        
        visited = set()
        def dfs(u):
            if u in visited:
                return
            visited.add(u)
            for nei in adj[u]:
                dfs(nei)
            return
        
        n_components = 0
        for i in range(n):
            print(i, visited)
            if i not in visited: 
                dfs(i)
                n_components += 1
        return n_components

        



