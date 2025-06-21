# https://leetcode.com/problems/first-missing-positive/

# Jun 21 2025
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        for i in range(len(nums)):
            val = abs(nums[i])
            if  1 <= val <= len(nums):
                if nums[val-1] > 0: 
                    nums[val-1] *= -1
                elif nums[val - 1] == 0:
                    nums[val-1] = -1 * (len(nums) + 1)
        for i in range(1, len(nums)+1):
            if nums[i-1] >= 0:
                return i
        return i + 1


# Nov 24 2023
def solution(nums):
    n = len(nums)
    for i in range(n):
        if 0 < nums[i] <= n:
            nums[i] *= -1
        else:
            nums[i] = -n-1

    # print(nums)
    for i in range(n):
        if 0 < abs(nums[i]) <= n:
            nums[abs(nums[i]) - 1] = abs(nums[abs(nums[i]) - 1])
    
    # print(nums)
    for i in range(n):
        if nums[i] < 0:
            return i+1
    return n+1

nums = [7,8,9,11,12]
assert solution(nums) == 1

nums = [1, 1]
assert solution(nums) == 2

nums = [1,2,0]
assert solution(nums) == 3

nums = [3,4,-1,1]
assert solution(nums) == 2
