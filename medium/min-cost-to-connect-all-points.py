# https://leetcode.com/problems/min-cost-to-connect-all-points/
# Prim's Algorithm on Undirectede Graphs (BFS)


def solution(points):
    n = len(points)
    graph = {}
    for i in range(n):
        graph[i] = []

    for i in range(n):
        for j in range(n): 
            if i != j:
                graph[i].append((
                    j, 
                    abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                ))


    minheap = [(0, 0)]
    visited = set()
    cost = 0
    edges_count  = 0
    while edges_count <  n:
        # print('<----', minheap)
        w1, s1 = heapq.heappop(minheap)
        if s1 in visited:
            continue
        visited.add(s1)
        cost += w1
        edges_count += 1
        for s2, w2 in graph[s1]:
            if s2 not in visited:
                heapq.heappush(minheap, (w2, s2))
        # print('---->', minheap)
    return cost


points = [[3,12],[-2,5],[-4,1]]
assert solution(points) == 18



        
