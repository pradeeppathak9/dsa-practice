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
        


# https://leetcode.com/problems/meeting-rooms-iii/

from collections import defaultdict
import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        freeRooms = list(range(n))     # min-heap of available room ids
        heapq.heapify(freeRooms)
        
        busyRooms = []                 # min-heap of (end_time, room)
        count = [0] * n
        
        for start, end in meetings: 
            # free up any rooms whose meetings have ended by `start`
            while busyRooms and busyRooms[0][0] <= start:
                end_t, room = heapq.heappop(busyRooms)
                heapq.heappush(freeRooms, room)

            if freeRooms:
                room = heapq.heappop(freeRooms)
                heapq.heappush(busyRooms, (end, room))
            else:
                end_t, room = heapq.heappop(busyRooms)
                heapq.heappush(busyRooms, (end_t + end - start, room))
            count[room] += 1
    return count.index(max(count))
