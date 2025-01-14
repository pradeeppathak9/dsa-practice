# https://leetcode.com/problems/network-delay-time/
# Dijksta Algorithm on Directed Graphs (BFS)

def solution(n, edges, src=0):
    graph = {}
    for s in range(n):
        graph[s] = []
        
    for s, d, w in edges:
        graph[s-1].append((d-1, w))
        
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
                
    return [ shortest.get(s, -1) for s in range(n) ]


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = solution(n=n, edges=times, src=k-1)
        return -1 if -1 in res else max(res)

        
