# https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/

def solution(n, edges, price): 
    graph = {i: [] for i in range(n) }
    
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])


    memo = {}
    def dfs(root, visited, cost):
        visited.add(root)
        max_cost = 0
        for neigh in graph[root]:
            if neigh not in visited:
                neigh_cost = dfs(neigh, visited, price[neigh])
                max_cost = max(max_cost, neigh_cost)
        return cost + max_cost
        
    max_cost = 0
    for root in range(n):
        cost = dfs(root, set(), price[root])
        max_cost = max(max_cost, cost - price[root])
    return max_cost
