# https://leetcode.com/problems/last-stone-weight/


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -1*s for s in stones]
        heapq.heapify(stones)
        while len(stones)> 1:
            x = -1*heapq.heappop(stones)
            y = -1*heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, -1*(x-y))
        return -1*stones[0] if len(stones) else 0


        
