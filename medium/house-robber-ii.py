# https://leetcode.com/problems/house-robber-ii/

def solution(nums):
    # case 1: decided to rob 1st house, that means cannot rob the last house
    last_state_1 = (0, nums[0]) 
    # cannot rob the next house because already robbed 1st house 
    last_state_1 = (max(last_state_1), max(last_state_1))
    
    # loop from 2 to n -1, because cannot robb the last house
    for i in range(2, len(nums) - 1):
        new_state = (max(last_state_1), last_state[0] + nums[i])
        last_state_1 = new_state
    print(last_state_1)
        
    
    # case 2: decided to not rob the 1st house, that means last house can be robbed
    last_state_2 = (0, 0)
    # loop from 1 to n, because last house can be robbed
    for i in range(1, len(nums)):
        new_state = (max(last_state_2), last_state_2[0] + nums[i])
        last_state_2 = new_state
    print(last_state_2)
    return max(max(last_state_1), max(last_state_2))
    
    
assert solution([2, 3, 2]) == 3
assert solution([1,2,3,1]) == 4
assert solution([1,2,3]) == 3
