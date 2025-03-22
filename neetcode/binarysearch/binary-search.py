# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
        return binarySearch(0, len(nums)-1)
            
        
            
        
