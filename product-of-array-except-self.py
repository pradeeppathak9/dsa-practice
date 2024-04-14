# https://leetcode.com/problems/product-of-array-except-self/

# def solution(nums):
#     n = len(nums)
#     prefix = [1] * len(nums)
#     suffix = [1] * len(nums)

#     for i in range(1, n):
#         prefix[i] = nums[i-1] * prefix[i-1]
#     for i in range(n-2, -1, -1):
#         suffix[i] = nums[i+1] * suffix[i+1]
#     return [ prefix[i]*suffix[i] for i in range(n) ] 

def solution(nums):
    n = len(nums)
    op = [1] * len(nums)
    
    tmp = 1
    for i in range(1, n):
        tmp = nums[i-1] * tmp
        op[i] *= tmp

    tmp = 1     
    for i in range(n-2, -1, -1):
        tmp = nums[i+1] * tmp
        op[i] *= tmp
    return op
            


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return solution(nums)
    
