# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/ 


def solution(nums):    
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = -1 * abs(nums[index])
    return [ i+1 for i in range(len(nums)) if nums[i] > 0]
    
    
nums = [4,3,2,7,8,2,3,1]
assert solution(nums) == [5, 6]
print("Done!")
