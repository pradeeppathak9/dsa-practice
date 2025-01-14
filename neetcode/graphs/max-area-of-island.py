# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        
        # 2d array, hence 4 directions to visit 
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(i, j):
            if i < 0 or i >= M or j <0 or j >= N:
                return 0
            if grid[i][j] == 0:
                return 0
            if grid[i][j] == -1:
                return 0            

            grid[i][j] = -1
            area = 1
            for d_i, d_j in directions:
                area += dfs(i + d_i, j + d_j)
            return area            

        max_area = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area
        

