# https://leetcode.com/problems/cheapest-flights-within-k-stops/

def solution(n, flights, src, dst, k):
    graph = {i:[] for i in range(n)}
    price = {}
    for (s, d, p) in flights:
        graph[s].append(d)
        price[(s, d)] = p        
    
    memo = {}
    def dfs(src, k):
        if src == dst: return 0
        if k == 0: return float('inf')

        ans = float('inf')
        for next_src in graph[src]:
            if (next_src, k-1) not in memo:
                res = dfs(next_src, k-1)
                memo[(next_src, k-1)] = res
            else:
                res = memo[(next_src, k-1)]
            
            ans = min(
                ans, price[(src, next_src)] + res
            )
        return ans
    
    ans = dfs(src, k+1)
    print("Total Calls Made ", calls_made)
    return ans if ans <  float('inf') else -1
        

##### test casessss
n = 10
src = 6
dst = 0
k = 7

flights = [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],
           [1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],
           [4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
print(solution(n, flights, src, dst, k))


n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
print(solution(n, flights, src, dst, k))
        

    
n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0

print(solution(n, flights, src, dst, k))



