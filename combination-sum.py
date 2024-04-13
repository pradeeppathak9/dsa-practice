# https://leetcode.com/problems/combination-sum/


def solution(candidates, target):
    res = set()
    def dfs(target, path=[]):
        if target == 0:
            res.add(tuple(sorted(path)))
        if target < 0:
            return
        for num in candidates:
            dfs(target - num, path + [ num ])
    dfs(target)
    return list(res)


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return solution(candidates, target)
        
