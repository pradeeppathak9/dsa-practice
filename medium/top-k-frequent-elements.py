# https://leetcode.com/problems/top-k-frequent-elements/

from collections import defaultdict
import heapq

def solution(nums, k):
    num_count = defaultdict(int)
    for n in nums:
        num_count[n] += 1
    
    num_count = [ (-v, k) for k, v in num_count.items()]
    heapq.heapify(num_count)
    return [heapq.heappop(num_count)[1] for i in range(k) ]
    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return solution(nums, k)
        
