# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    matrix[i][j] += matrix[i][j-1] 
                elif j == 0:
                    matrix[i][j] += matrix[i-1][j]
                else: 
                    matrix[i][j] += matrix[i][j-1] + matrix[i-1][j]  - matrix[i-1][j-1] 
        self.matrix = matrix
        print(self.matrix)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.matrix[row2][col2]
        if row1 > 0:
            res -= self.matrix[row1-1][col2]
        if col1 > 0:
            res -= self.matrix[row2][col1-1]
        if row1 >0 and col1 >0:
            res += self.matrix[row1-1][col1-1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
