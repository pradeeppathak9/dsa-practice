# https://leetcode.com/problems/house-robber/

def solution(nums):
    last_state = (0, nums[0]) 
    # Index 
    # 0 -> not robbing current house, max_profit = max of (last house robbed, last house not robbed)
    # 1 -> robbing current house, max_profit = max_profit_if_last_house_not_robbed + this house
    for i in range(1, len(nums)):
        new_state = (max(last_state), last_state[0] + nums[i])
        last_state = new_state
    return max(last_state)

    

assert solution([2,7,9,3,1]) == 12
assert solution([1,2,3,1]) == 4
assert solution([2,1,1,2]) == 4
    
    
    
    
