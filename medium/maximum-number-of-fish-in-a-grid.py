# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if ( r < 0 or c < 0
                or r >= rows or c >= cols
                or (r, c) in visited or grid[r][c] == 0):
                return 0

            visited.add((r, c))
            res = grid[r][c]

            for (nr, nc) in [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]:
                res += dfs(nr, nc) 
            return res
            
        rows, cols = len(grid), len(grid[0])
        visited = set()
        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c))
        return res






        
