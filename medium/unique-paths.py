# https://leetcode.com/problems/unique-paths/


# bottom up solution ~ DP
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m-1):
            new_row = [1] * n
            for j in range(n-2, -1, -1):
                new_row[j] = new_row[j+1] + row[j]
            row = new_row
        return row[0]
        

# top - down solution ~ DFS + memoization
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def dfs(i, j):
            if i >= m or j >= n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            if (i, j) in dp:
                return dp[(i, j)]
            dp[(i, j)] = dfs(i+1, j) + dfs(i, j+1)
            return dp[(i, j)]
        return dfs(0, 0)


assert solution(3, 2) == 3
assert solution(3, 7) == 28
