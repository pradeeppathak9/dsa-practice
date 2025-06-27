# https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i, total):
            if total == amount:
                return 1
            if total > amount or i == len(coins):
                return 0
            if (i, total) in dp:
                return dp[(i, total)]

            pick = dfs(i, total + coins[i])
            skip = dfs(i + 1, total)
            dp[(i, total)] = pick + skip
            return dp[(i, total)]
        return dfs(0, 0)
