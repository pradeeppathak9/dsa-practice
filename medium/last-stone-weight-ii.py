# https://leetcode.com/problems/last-stone-weight-ii/

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = ceil(stoneSum/2)

        dp = {}
        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (stoneSum - total))
            if (i, total) in dp:
                return dp[(i, total)]
            dp[(i, total)] = min(
                dfs(i+1, total + stones[i]),
                dfs(i+1, total)
            )
            return dp[(i, total)]
        return dfs(0, 0)






