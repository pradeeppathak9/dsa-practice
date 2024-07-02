# https://leetcode.com/problems/the-number-of-beautiful-subsets/



class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        res = []
        def backtrack(start, path):
            nonlocal res
            if len(path):
                res += [ path ]
            for i in range(start, len(nums)):
                skip = False
                for j in range(len(path), 0, -1):
                    if nums[i] - path[j-1] == k:
                        skip = True
                        break
                    if nums[i] - path[j-1] > k:
                        break
                if skip:
                    continue
                backtrack(i+1, path + [ nums[i] ])
        backtrack(0, [])
        # print(res)
        return len(res)



        
