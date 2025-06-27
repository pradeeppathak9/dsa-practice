# https://leetcode.com/problems/distinct-subsequences/

# top-down
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = {}
        def dfs(i, j):
            if j == n:
                return 1
            if i == m:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            if s[i] == t[j]:
                res = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                res = dfs(i + 1, j)
            dp[(i, j)] = res
            return res
        return dfs(0, 0)

# bottom up
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, m + 1):
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
        return dp[n]
