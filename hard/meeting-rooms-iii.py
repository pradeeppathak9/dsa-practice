# https://leetcode.com/problems/meeting-rooms-iii/

from collections import defaultdict
import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        minHeap = []
        result = defaultdict(int)
        status = defaultdict(int)
        
        for (start, end) in sorted(meetings): 
            while minHeap and minHeap[0][0] <= start:
                end_t, room = heapq.heappop(minHeap)
                status[room] = 0

            if len(minHeap) == n:
                end_t, room = heapq.heappop(minHeap)
                heapq.heappush(minHeap, (end_t + end - start, room))
            else:
                for room in range(n):
                    if status[room] == 0:
                        break
                status[room] = 1
                heapq.heappush(minHeap, (end, room))
            result[room] += 1
          
        ans = (0, 0)
        for room, no_of_meetings in result.items():
            if no_of_meetings > ans[1]:
                ans = (room, no_of_meetings)
        return ans[0]
        
