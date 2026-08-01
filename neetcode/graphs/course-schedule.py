# https://leetcode.com/problems/course-schedule/

# Kahn's Algorithm (BFS)

from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        queue = deque([c for c in range(numCourses) if in_degree[c] == 0])
        order = []
        
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return len(order) == numCourses
        

# DFS alternative (cycle detection via coloring)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        state = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited

        def hasCycle(node):
            if state[node] == 1:
                return True  # found a cycle
            if state[node] == 2:
                return False  # already checked, no cycle here

            state[node] = 1  # mark as visiting
            for neighbor in graph[node]:
                if hasCycle(neighbor):
                    return True

            state[node] = 2  # mark as visited
            return False

        for i in range(numCourses):
            if hasCycle(i):
                return False

        return True

        
