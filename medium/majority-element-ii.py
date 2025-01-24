# https://leetcode.com/problems/majority-element-ii/


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k = int(len(nums) / 3)
        nums = sorted(nums)
        start = 0
        res = []
        for i in range(len(nums)):
            if nums[i] != nums[start]:
                if i - start> k:
                    res.append(nums[start])
                start = i
        if i - start + 1> k:
            res.append(nums[start])
        return res

                
        
