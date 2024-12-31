# https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # top down solution
        cache = {len(days): 0}
        res = costs[0] * len(days)
        def dfs(i):
            if i in cache:
                return cache[i]

            cache[i] = float("inf")
            for cost, duration in zip(costs, [1, 7, 30]):
                j = i
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1
                cache[i] = min(cache[i], cost + dfs(j))
            return cache[i]
        return dfs(0)


        # bottom up solution
        dp = [0] * (len(days) + 1)
        for i in reversed(range(len(days))):
            dp[i] = float("inf")
            for cost, duration in zip(costs, [1, 7, 30]):
                j = i
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1
                dp[i] = min(dp[i], cost + dp[j])
        return dp[0]









        


        
