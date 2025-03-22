# https://leetcode.com/problems/k-closest-points-to-origin/

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distances = [ (-1*((x**2) + (y**2))**0.5, x, y) for (x, y) in points ] 
        heapq.heapify(distances)
        while len(distances) > k:
            heapq.heappop(distances)
        return [ (x,y) for (dist, x, y) in distances]

        
