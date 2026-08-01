# https://leetcode.com/problems/minimum-height-trees/


from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]  # single node is its own root, trivially height 0

        # Build adjacency list
        graph = [set() for _ in range(n)]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        leaves = deque(i for i in range(n) if len(graph[i]) == 1)
        remaining = n
        while remaining > 2:
            num_leaves = len(leaves)
            remaining -= num_leaves
            for _ in range(num_leaves):
                leaf = leaves.popleft()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)
        
        return list(leaves)
        
