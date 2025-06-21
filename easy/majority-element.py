# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = -1
        count = 0
        for num in nums:
            if count == 0:
                ans = num
                count += 1
            else:
                if num == ans:
                    count += 1
                else:
                    count -= 1
        return ans


