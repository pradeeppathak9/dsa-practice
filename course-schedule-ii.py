# https://leetcode.com/problems/course-schedule-ii/
# Topological Sort (DFS)

def solution(numCourses, prerequisites):
    graph = { i: [] for i in range(numCourses) }
    for u, v in prerequisites:
        graph[u].append(v)
    res = []
    visited = set()
    
    def dfs(u):
        if u in visited:
            return False
        visited.add(u)
        for v in graph[u]:
            if not dfs(v):
                return False
        if u not in res:
            res.append(u)
        visited.remove(u)
        graph[u] = []
        return True

    for i in range(numCourses):
        if i not in res:
            if not dfs(i):
                return []
    return res 

numCourses = 2
prerequisites = [[0,1]]
solution(numCourses, prerequisites)
# [1, 0]


numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
solution(numCourses, prerequisites)
# [0, 1, 2, 3]
