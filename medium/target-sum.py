# https://leetcode.com/problems/target-sum/


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # index, curr_sum

        def backtrack(index, curr_sum):
            if (index, curr_sum) in dp:
                return dp[(index, curr_sum)]

            if index == len(nums):
                return 1 if curr_sum == target else 0
            
            dp[(index, curr_sum)] = (
                backtrack(index + 1, curr_sum + nums[index]) +
                backtrack(index + 1, curr_sum - nums[index])
            )
            
            return dp[(index, curr_sum)]

        return backtrack(0, 0)
        
