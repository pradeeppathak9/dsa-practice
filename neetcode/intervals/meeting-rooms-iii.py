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
