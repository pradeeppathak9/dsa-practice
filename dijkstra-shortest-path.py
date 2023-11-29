# Dijkstra's Algorithm for Shortest Path in a directed edge

def solution(n, edges, src=0):
    graph = {}
    for s in range(n):
        graph[s] = []
        
    for s, d, w in edges:
        graph[s].append((d, w))
        
    shortest = {}
    minheap = [(0, src)] # (total weight, dest) 
    
    while minheap:
        w1, s1 = heapq.heappop(minheap)
        if s1 in shortest:
            # already visited
            continue
        shortest[s1] = w1
        for s2, w2 in graph[s1]:
            if s2 not in shortest:
                heapq.heappush(minheap, (w1 + w2, s2))
                
    for i in range(n):
        if s in shortest:
            # already visited
            continue
        shortest[s] = -1
    return shortest
        

n = 5
edges = [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]]
src = 0
solution(n, edges, src)
# {0: 0, 2: 3, 4: 5, 1: 7, 3: 9}
