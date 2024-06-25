# https://leetcode.com/problems/first-missing-positive/

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
