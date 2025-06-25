# https://leetcode.com/problems/trapping-rain-water/

# cleaned solution
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        ans = 0
        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])    
                ans += l_max - height[l]
            else:
                r-=1
                r_max = max(r_max, height[r])
                ans += r_max - height[r]
        return ans


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max = height[0]
        r_max = height[-1]
        ans = 0
        while l <= r:
            if l_max <= r_max:
                diff = min(l_max, r_max) - height[l] 
                l_max = max(l_max, height[l] )
                ans += max(diff, 0)
                l+=1
            else:
                diff = min(l_max, r_max) - height[r] 
                r_max = max(r_max, height[r])
                ans += max(diff, 0)
                r-=1
        return ans



                






