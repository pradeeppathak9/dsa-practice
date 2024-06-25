# https://leetcode.com/problems/first-completely-painted-row-or-column/


from collections import defaultdict
def solution(arr, mat):
    mat_map = {}
    m, n = len(mat), len(mat[0])
    for i in range(m):
        for j in range(n):
            mat_map[mat[i][j]] = (i, j)
    row_count = defaultdict(int)
    column_count = defaultdict(int)
    
    i = 0
    for el in arr:
        row, col = mat_map[el]
        row_count[row] += 1
        column_count[col] += 1
        if row_count[row] == n or column_count[col] == m:
            break
        i+=1
    return i
        
