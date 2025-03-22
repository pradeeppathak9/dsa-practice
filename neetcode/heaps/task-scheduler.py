# https://leetcode.com/problems/task-scheduler/

# from collections import Counter
# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         time = 0
#         last_execution_time = {}

#         tasks = [(-1*v, k) for k, v in Counter(tasks).items()]
#         heapq.heapify(tasks)
#         while len(tasks): 
#             time += 1
#             stack = []
#             while len(tasks):
#                 count, task = heapq.heappop(tasks)
#                 if not last_execution_time.get(task) or time - last_execution_time.get(task) > n:
#                     count += 1
#                     last_execution_time[task] = time
#                     if count != 0:
#                         stack.append((count, task))
#                     break
#                 stack.append((count, task))
#             while len(stack):
#                 heapq.heappush(tasks, stack.pop())
#         return time
            

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-1*cnt for cnt in count.values() ]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q: 
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time


            


            


        
