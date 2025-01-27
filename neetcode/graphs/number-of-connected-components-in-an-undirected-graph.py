# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

def solution(n, edges):
    adj = { i: [] for i in range(n) }
    for (u, v) in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = set()
    def dfs(u):
        if u in visited:
            return
        visited.add(u)
        for nei in adj[u]:
            dfs(nei)
        return
      
    n_components = 0
    for i in range(n):
        print(i, visited)
        if i not in visited: 
            dfs(i)
            n_components += 1
    return n_components
    

        
