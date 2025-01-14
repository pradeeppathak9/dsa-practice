# https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M, N = len(heights), len(heights[0])
        
        pa_visited = set()
        at_visited = set()

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(i, j, visited, start_value):
            if i < 0 or j < 0 or i >= M or j >= N:
                return

            if (i, j) in visited:
                return

            if heights[i][j] < start_value:
                return

            visited.add((i, j))
            for (di, dj) in directions:
                dfs(i + di, j + dj, visited, heights[i][j])
            
        for i in range(N):
            dfs(0, i, pa_visited, heights[0][i])
            dfs(M-1, i, at_visited, heights[M-1][i])

        for i in range(M):
            dfs(i, 0, pa_visited, heights[i][0])
            dfs(i, N-1, at_visited, heights[i][N-1])

        return list(pa_visited.intersection(at_visited))









     
        
            

            

        
