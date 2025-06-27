
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = {}
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            res = 1
            for dx, dy in [ (0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    res = max(res, 1 + dfs(x, y))
            dp[(i, j)] = res
            return res
        return max(dfs(i, j) for i in range(m) for j in range(n))
