# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        n = len(nums)
        target = total // 2

        dp = {}
        def dfs(i, target):
            if target == 0:
                return True
            if target < 0 or i == len(nums):
                return False 
            if (i, target) in dp:
                return dp[(i, target)]

            dp[(i, target)] = dfs(i+1, target - nums[i]) or dfs(i+1, target)
            return dp[(i, target)]
        return dfs(0, target)
