# https://leetcode.com/problems/coin-change/


def solution(coins, amount):
    dp = [-1 for i in range(amount + 1) ]
    dp[0] = 0
    for i in range(1, amount+1):
        for deno in coins:
            if i - deno > 0:
                if dp[i - deno] != -1:
                    dp[i] = min(dp[i], dp[i - deno] + 1) if dp[i] != -1 else dp[i - deno] + 1        
            if i - deno == 0:
                dp[i] = 1
    print(dp)
    return dp[-1]

coins, amount = [1,2,5] , 11
assert solution(coins, amount) == 3

coins, amount = [1, 2, 5], 100
assert solution(coins, amount) == 20

coins, amount = [1], 0
assert solution(coins, amount)  == 0

coins, amount = [2], 3
assert solution(coins, amount) == -1


coins, amount = [2,5,10,1], 27
assert solution(coins, amount) == 4
