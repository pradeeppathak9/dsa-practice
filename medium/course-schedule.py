# https://leetcode.com/problems/course-schedule/


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


def solution(numCourses, prerequisites):
    graph = { i: [] for i in range(numCourses) }
    for u, v in prerequisites:
        graph[u].append(v)

    visited = set()
    path = set()

    def dfs(u):
        if u in path: return False
        if u in visited: return True

        path.add(u)
        for v in graph[u]:
            if not dfs(v):
                return False
        path.remove(u)
        visited.add(u)
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False
    return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return solution(numCourses, prerequisites)
        
