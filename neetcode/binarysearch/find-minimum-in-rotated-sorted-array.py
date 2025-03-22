# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        def findMinIndexInRotatedSortedArray(nums):
            left, right = 0, len(nums)-1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            return left
        min_index = findMinIndexInRotatedSortedArray(nums)
        return nums[min_index]
        
        

        
