# https://leetcode.com/problems/count-servers-that-communicate/


from collections import defaultdict
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_server_count = defaultdict(int)
        col_server_count = defaultdict(int)
        for i in range(m):
            for j in range(n):
                row_server_count[i] += grid[i][j]
                col_server_count[j] += grid[i][j]

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += int(max(row_server_count[i], col_server_count[j]) > 1)
        return res


        
