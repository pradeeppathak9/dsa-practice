## https://leetcode.com/problems/partition-array-for-maximum-sum/

# recursion with memoization
def solution(arr, k):
    cache = {}
    
    def dfs(i):
        if i > len(arr):
            return 0 
        if i in cache:
            return cache[i]
    
        res = 0
        window_max = 0
        for j in range(i, min(len(arr), i+k)):
            window_size = j-i+1
            window_max = max(window_max, arr[j])
            res = max(res, window_max*window_size + dfs(j+1)) 
            
        cache[i] = res
        return res
    return dfs(0)


##  dp solution
def solution(arr, k):
    dp = [0 for i in range(len(arr))]

    for i in range(0, len(arr)):
        for j in range(i, i-k, -1):    
            if j < 0:
                break
            sub_sum = dp[j-1] if j >0 else 0
            dp[i] = max(dp[i], sub_sum + max(arr[j:i+1]) * (i-j+1))
            # print(i, j, dp)
    return dp[-1]
  
