# https://leetcode.com/problems/course-schedule-ii/


from collections import defaultdict, deque

# Kahn’s Algorithm (BFS)
def findOrder(numCourses, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    # Build graph and in-degree array
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Start with courses that have no prerequisites
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If all courses taken, return the order
    if len(order) == numCourses:
        return order
    else:
        return []  # cycle detected → impossible



def solution(numCourses, prerequisites):
    graph = { i: [] for i in range(numCourses) }
    for u, v in prerequisites:
        graph[u].append(v)

    res = []
    visited = set()
    path = set()

    def dfs(u):
        if u in path:
            return False
        if u in visited:
            return True

        path.add(u)
        for v in graph[u]:
            if not dfs(v):
                return False
        path.remove(u)

        visited.add(u)
        res.append(u)
        return True

    for i in range(numCourses):
        if not dfs(i):
            return []
    return res 



class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        return solution(numCourses, prerequisites)
        
