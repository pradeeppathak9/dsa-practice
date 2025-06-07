# https://leetcode.com/problems/min-cost-climbing-stairs/

# DP - Bottom Up
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost) -3, -1, -1 ):
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])



# DFS - Top Down
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            dp[i] = min(
                dp[i-1] + cost[i-1], 
                dp[i-2] + cost[i-2]
            )
        return dp[-1]

