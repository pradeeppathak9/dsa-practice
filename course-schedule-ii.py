# https://leetcode.com/problems/course-schedule-ii/
# Topological Sort (DFS)

def solution(numCourses, prerequisites):
    graph = { i: [] for i in range(numCourses) }
    for u, v in prerequisites:
        graph[u].append(v)

    res = []
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
        res.append(u)
        return True

    for i in range(numCourses):
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
