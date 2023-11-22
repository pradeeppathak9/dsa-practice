# https://leetcode.com/problems/unique-paths/

def solution(m, n):
    dp =  [[1 for i in range(n)] for j in range(m)] 
    for i in range(m):
        for j in range(n):
            if i > 0 and j > 0 :
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            elif i > 0:
                dp[i][j] = dp[i-1][j]
            elif j > 0:
                dp[i][j] = dp[i][j-1]
    print(dp)
    return dp[-1][-1]


assert solution(3, 2) == 3
assert solution(3, 7) == 28
