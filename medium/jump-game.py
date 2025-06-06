# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_idx = 0
        for i in range(len(nums)-1):
            if i > max_idx:
                return False
            max_idx = max(max_idx, i + nums[i])
            # print(i, nums[i], max_idx)
        return max_idx >= len(nums) -1


        
