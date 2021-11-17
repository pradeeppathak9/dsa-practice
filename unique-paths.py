# https://leetcode.com/problems/unique-paths/

def solution(m, n):
    dp = [[0]*(n+1) for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if i == 1 and j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    return dp[-1][-1]
        
print(solution(7, 3))
