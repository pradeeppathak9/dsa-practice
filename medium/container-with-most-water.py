# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        def solution(height):
            l, r = 0, len(height) - 1
            max_vol = 0
            max_index = None
            while r > l:
                vol = min(height[l], height[r]) * (r-l)
                if max_vol < vol:
                    max_vol = vol
                    max_index= (l, r)
                if height[l] < height[r]:
                    l +=1
                else:
                    r -=1

            print(max_index, max_vol)
            return max_vol
        return solution(height)
            
