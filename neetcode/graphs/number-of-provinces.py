# https://leetcode.com/problems/number-of-provinces/


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parents = [node for node in range(len(isConnected))]
        rank = [1] * len(parents)

        def find(node):
            res = node
            while res != parents[res]:
                parents[res] = parents[parents[res]]
                res = parents[res]
            return res 

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0

            if rank[p1] > rank[p2]:
                parents[n2] = p1
                rank[p1] += 1
            else:
                parents[n1] = p2
                rank[p2] += 1
            return 1
             
        result = len(parents)
        for n1 in range(len(isConnected)):
            for n2 in range(len(isConnected)):
                if isConnected[n1][n2] == 1:
                    result -= union(n1, n2)
        return result   
        
