# https://leetcode.com/problems/course-schedule-ii/

# Kahn's Algorithm (BFS)

from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
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
        
        return order if len(order) == numCourses else []


# DFS alternative (cycle detection via coloring)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # 0 = unvisited, 1 = visiting (in current DFS path), 2 = fully visited
        state = [0] * numCourses
        order = []
        
        def dfs(node):
            if state[node] == 1:
                return False  # cycle detected
            if state[node] == 2:
                return True   # already processed
            
            state[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            state[node] = 2
            order.append(node)  # post-order: add after all dependents processed
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return order[::-1]  # reverse post-order = topological order
