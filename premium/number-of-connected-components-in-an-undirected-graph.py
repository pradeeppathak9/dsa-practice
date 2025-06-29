# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
from collections import defaultdict

def countComponents(n, edges):
    # Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * n

    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1

    return count

# Example usage
n = 5
edges = [[0,1],[1,2],[3,4]]
print(countComponents(n, edges))  # Output: 2



def countComponents(n, edges):
    parent = [i for i in range(n)]

    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]  # Path compression
            x = parent[x]
        return x

    def union(x, y):
        root_x, root_y = find(x), find(y)
        if root_x != root_y:
            parent[root_y] = root_x

    for u, v in edges:
        union(u, v)

    # Count unique roots
    return len(set(find(i) for i in range(n)))

# Example usage
n = 5
edges = [[0,1],[1,2],[3,4]]
print(countComponents(n, edges))  # Output: 2

        
