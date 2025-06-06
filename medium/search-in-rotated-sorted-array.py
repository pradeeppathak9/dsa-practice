# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
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

        def binarySearch(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return -1
            
        return max(binarySearch(0, min_index-1), binarySearch(min_index, len(nums)-1))
