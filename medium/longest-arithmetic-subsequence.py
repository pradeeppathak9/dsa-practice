# https://leetcode.com/problems/longest-arithmetic-subsequence/

from collections import defaultdict

def longest_arithmetic_seq_by_steps(nums, steps=1):
    subsequence_len = defaultdict(int)
    res = 0
    for n in nums: 
        subsequence_len[n] = subsequence_len[n - steps] + 1
        res = max(res, subsequence_len[n])
    # print(steps, subsequence_len)
    return res

def solution(nums):
    res = 0
    for i in range(0, max(nums)+ 1):
        res = max(
            res, 
            longest_arithmetic_seq_by_steps(nums, i),
            longest_arithmetic_seq_by_steps(nums, -i)
        )
    return res


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        return solution(nums)
