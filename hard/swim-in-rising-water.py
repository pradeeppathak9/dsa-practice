# https://leetcode.com/problems/swim-in-rising-water/

import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = [(grid[0][0], (0, 0))]
        visited = {}
        while queue:
            cost, (i, j) = heapq.heappop(queue)
            if (i, j) in visited:
                continue
            visited[(i, j)] = cost
            if i == m-1 and j == n-1:
                break
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    if (x, y) in visited:
                        continue
                    heapq.heappush(queue, (max(cost, grid[x][y]), (x, y)))
        return cost
