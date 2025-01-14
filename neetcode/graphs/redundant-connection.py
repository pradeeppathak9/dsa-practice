# https://leetcode.com/problems/redundant-connection/

class UnionFind:
    def __init__(self,n):
        self.par = [i for i in range(n+1)]
        self.rank = [1]*(n+1)

    def find(self,x):
        while x!=self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        
        return x

    def union(self,n1,n2):
        p1,p2 = self.find(n1),self.find(n2)
        if p1==p2:
            return False
        
        if self.rank[p1]<self.rank[p2]:
            self.rank[p2]+=self.rank[p1]
            self.par[p1]=self.par[p2]
        else:
            self.rank[p1]+=self.rank[p2]
            self.par[p2]=self.par[p1]

        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ans = 0
        uf = UnionFind(len(edges))

        for a,b in edges:
            if not uf.union(a,b):
                return [a,b]
        
