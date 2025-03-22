# https://leetcode.com/problems/combination-sum/

# def solution(candidates, target):
#
#     res = set()
#     def bfs(target, path=[]):
#         if target == 0:
#             res.add(tuple(sorted(path)))
#         if target < 0:
#             return
#         for num in candidates:
#             bfs(target - num, path+[num])
#     bfs(target)
#     return list(res)


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        def dfs(idx, cur, path):
            if cur > target: return
            if cur == target:
                res.append(path)
                return
            for i in range(idx, len(candidates)):
                dfs(i, cur+candidates[i], path+[candidates[i]])
        dfs(0, 0, [])
        return res
        
