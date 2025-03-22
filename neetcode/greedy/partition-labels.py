# https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i, c in enumerate(s):
            last_index[c] = i

        res = []
        start = end = 0
        for i, c in enumerate(s):
            end = max(end, last_index[c])
            if i == end:
                res.append(end - start + 1)
                start = end = i+1
        return res
