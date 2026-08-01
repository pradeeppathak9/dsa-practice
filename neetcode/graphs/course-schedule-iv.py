# https://leetcode.com/problems/course-schedule-iv/


# Approach 1 — Floyd-Warshall

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reachable = [[False] * numCourses for _ in range(numCourses)]
        
        for a, b in prerequisites:
            reachable[a][b] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if reachable[i][k] and reachable[k][j]:
                        reachable[i][j] = True

        return [reachable[u][v] for u, v in queries]


# BFS
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        reachable = [set() for _ in range(numCourses)]

        for start in range(numCourses):
            queue = deque(graph[start])
            visited = set(graph[start])
            while queue:
                node = queue.popleft()
                reachable[start].add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)


        return [v in reachable[u] for u, v in queries]









        


        

