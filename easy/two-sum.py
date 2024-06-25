# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = { n: i for i, n in enumerate(nums) }
        nums = [ target - n for n in nums ]
        
        for i, bal in enumerate(nums):
            if bal in num_index:
                if i != num_index[bal]:
                    return (i, num_index[bal])
        
