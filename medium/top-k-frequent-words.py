# https://leetcode.com/problems/top-k-frequent-words/


import collections
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = collections.Counter(words)
        heap = [ (-v, k) for k, v in word_count.items()]
        heapq.heapify(heap)
        return [ heapq.heappop(heap)[1] for i in range(k) ]
