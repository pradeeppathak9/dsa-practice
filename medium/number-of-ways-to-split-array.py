# https://leetcode.com/problems/number-of-ways-to-split-array/

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        r_sum = sum(nums)
        ans = l_sum = 0
        for i in range(len(nums) - 1):
            l_sum += nums[i]
            r_sum -= nums[i]
            if l_sum >= r_sum:
                ans += 1
        return ans 
