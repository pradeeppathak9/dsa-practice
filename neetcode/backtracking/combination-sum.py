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
        candidates = sorted(candidates)
        res = []
        def dfs(index, balance, path=[]):
            if balance == 0:
                res.append(path)
                return
            if index >= len(candidates) or balance < 0: 
                return 
            dfs(index, balance - candidates[index], [*path, candidates[index]])
            dfs(index + 1, balance, path)

        dfs(0, target, [])
        return res
        
