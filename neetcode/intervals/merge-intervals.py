# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        results = [ intervals.pop(0) ]
        
        while len(intervals):
            if intervals[0][0] <= results[-1][1]:
                left = results.pop(-1)
                right = intervals.pop(0)
                results.append([min(left[0], right[0]), max(left[1], right[1])])
            else:
                results.append(intervals.pop(0))
            # print(results, intervals)
        return results



        
