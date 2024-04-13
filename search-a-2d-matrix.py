# https://leetcode.com/problems/search-a-2d-matrix/

def solution(matrix, target):
    def binary_search(arr, target):
        start, end = 0, len(arr)
        while start <= end:
            center = (start + end)//2
            if arr[center] == target:
                return True
            if target < arr[center]:
                end = center - 1
            else:
                start = center + 1
        return False
    
    for i in range(len(matrix)):
        if matrix[i][0] <= target <= matrix[i][-1]:
            return binary_search(matrix[i], target)
    return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return solution(matrix, target)
        
