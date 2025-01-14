# https://leetcode.com/problems/course-schedule/

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
        
