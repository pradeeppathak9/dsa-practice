# https://leetcode.com/problems/minimum-time-difference


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time_in_numeric = []
        for time in timePoints:
            hh, mm = time.split(":")
            hh, mm = int(hh), int(mm)
            time_in_numeric.append( hh*60 + mm)
        time_in_numeric = sorted(time_in_numeric)
        ans = 60*24 - time_in_numeric[-1] + time_in_numeric[0]
        for i in range(1, len(time_in_numeric)):
            ans= min(ans, time_in_numeric[i] - time_in_numeric[i-1])
        return ans





        
