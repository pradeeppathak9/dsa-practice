# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                par[p2] = par[p1]
                rank[p1] += 1
            else:
                par[p1] = par[p2]
                rank[p2] += 1
            return 1
        
        res = n
        for u, v in edges:
            res -= union(u, v)
        return res 
            
            
        

