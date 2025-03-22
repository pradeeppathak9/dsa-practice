# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(counter, path):
            if len(path) == len(nums):
                res.append(path)
                return

            for x in counter:
                if counter[x]:
                    counter[x] -= 1
                    dfs(counter, path + [x])
                    counter[x] += 1
        dfs(Counter(nums), [])
        return res






        
        
