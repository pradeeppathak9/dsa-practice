# https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}

        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            safe[i] = True
            return True

        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res

        # unsafe_nodes = set()
    
        # def dfs(node, path = set()):
        #     if node in path or node in unsafe_nodes:
        #         # circular path
        #         for n in path:
        #             unsafe_nodes.add(n)
        #         return 

        #     path.add(node)
        #     for neigh in graph[node]:
        #         dfs(neigh, path)
        #     path.remove(node)

        # for i in range(len(graph)):
        #     if i not in unsafe_nodes:
        #         dfs(i)
        # return [i for i in range(len(graph)) if i not in unsafe_nodes ]


