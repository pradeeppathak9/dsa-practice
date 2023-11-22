# https://leetcode.com/problems/jump-game/

# bottom up approach with dp, calculate min jump require to reach ith position

def solution(nums):
    dp = [None] * len(nums)
    for i in range(len(nums)):
        if i == 0:
            dp[i]=0
        for j in range(nums[i]):
            if i + j + 1 >= len(nums):
                break
                
            if dp[i+j+1] is None:
                dp[i+j+1] = dp[i]+1 
            else:
                dp[i+j+1] = min(dp[i]+1, dp[i+j+1])
    print(dp)
    return dp[-1] is not None
            

# test cases
nums = [3,2,1,0,4]
assert solution(nums) == False

nums = [2,3,1,1,4]
assert solution(nums) == True
            
nums = [5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]
assert solution(nums) == True

        
