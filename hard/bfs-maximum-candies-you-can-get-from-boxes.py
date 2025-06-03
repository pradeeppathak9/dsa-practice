# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        avl_boxes = set() # list of all accessible boxes

        queue = deque() # queue of boxes that can be visited next
        for box in initialBoxes:
            avl_boxes.add(box)
            if status[box]:
                queue.append(box)

        visited = set()
        candies_collected = 0
        while queue:
            i = queue.popleft()
            if i in visited:
                continue
            visited.add(i)
            candies_collected += candies[i]

            # process new available boxes 
            for b in containedBoxes[i]: 
                avl_boxes.add(b) # add to available box
                if status[b]: # check if the box can be opened 
                    if b not in visited: #and is not already visited
                        queue.append(b)
                    
            # process new available keys 
            for b in keys[i]:
                status[b] = True # this box can be opened
                if b in avl_boxes: # check if the box is accessible 
                    if b not in visited: # and is not already visited
                        queue.append(b)

        return candies_collected


            
            



        
