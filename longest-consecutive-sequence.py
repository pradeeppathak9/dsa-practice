# https://leetcode.com/problems/longest-consecutive-sequence/submissions/

def solution(nums):
    num_set = set(nums)
    visited = {}
    def dfs(n):
        if n in visited:
            return
        if n-1 not in num_set:
            visited[n] = 1
            return
        dfs(n-1)
        visited[n] = visited[n-1] + 1 

    ans = 0
    for n in num_set:
        if n not in visited:
            dfs(n)
        ans = max(ans, visited[n])
    return ans


nums = [100, 4, 200, 1, 3, 2]
assert solution(nums) == 4
