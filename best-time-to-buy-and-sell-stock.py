# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def solution(prices):
    buy = prices[0]
    profit = 0
    for n in prices:
        if n < buy:
            buy = n
        profit = max(profit, n - buy)
    return profit
            
            
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return solution(prices)
        
