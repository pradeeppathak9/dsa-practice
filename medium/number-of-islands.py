# https://leetcode.com/problems/number-of-islands/
# DFS

def solution(grid):
    m, n = len(grid), len(grid[0])
    visited = set()
    
    def dfs(i, j):
        visited.add((i, j))
        # 2d array, hence 4 directions to visit 
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for d in directions:
            next_i, next_j = i+d[0], j+d[1]
            # print("---", next_i, next_j)
            if 0 <= next_i < m and 0 <= next_j < n:
                if grid[next_i][next_j] == "1" and (next_i, next_j) not in visited:
                    dfs(next_i, next_j)
    output = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1" and (i, j) not in visited:
                # new island
                # print("new island", i, j)
                output += 1
                dfs(i, j)
    return output



grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

assert solution(grid) == 3
