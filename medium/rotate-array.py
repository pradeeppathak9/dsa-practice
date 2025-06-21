# https://leetcode.com/problems/rotate-array/


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        def reverse_array(start, end):
            while 0 <= start < end < len(nums):
                nums[start], nums[end] = nums[end], nums[start]
                start+=1
                end-=1
        reverse_array(0, len(nums)-1)
        reverse_array(0, k-1)
        reverse_array(k, len(nums)-1)

        



